import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="✨",
    layout="wide"
)

# CSS Custom
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stChatMessage {
        background-color: #1a1d24;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    .stChatMessage[data-testid="user"] {
        background-color: #1e2936;
    }
    .stChatMessage[data-testid="assistant"] {
        background-color: #1a1d24;
    }
    div[data-testid="stSidebar"] {
        background-color: #0e1117;
        border-right: 1px solid #262730;
    }
    .stButton button {
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    h1 {
        color: #ffffff;
        font-weight: 600;
    }
    .stMetric {
        background-color: #1a1d24;
        padding: 1rem;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_key" not in st.session_state:
    try:
        st.session_state.api_key = st.secrets["GEMINI_API_KEY"]
    except:
        st.session_state.api_key = "YOUR_API_KEY_HERE"  # fallback

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

if "persona" not in st.session_state:
    st.session_state.persona = "helpful"

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

# Persona definitions
PERSONAS = {
    "helpful": {
        "name": "Asisten Ramah",
        "prompt": "Kamu adalah asisten AI yang sangat membantu dan ramah. Jawab dengan jelas dan informatif.",
        "icon": "🤝"
    },
    "professional": {
        "name": "Profesional",
        "prompt": "Kamu adalah konsultan bisnis profesional. Berikan jawaban yang terstruktur dan formal.",
        "icon": "💼"
    },
    "creative": {
        "name": "Kreatif",
        "prompt": "Kamu adalah AI yang kreatif dan imajinatif. Jawab dengan cara yang unik dan menarik.",
        "icon": "🎨"
    },
    "technical": {
        "name": "Teknis",
        "prompt": "Kamu adalah ahli teknologi. Berikan penjelasan teknis yang detail dan akurat.",
        "icon": "⚙️"
    }
}

# Sidebar
with st.sidebar:
    st.title("⚙️ Pengaturan Chatbot")
    
    st.divider()
    
    # Persona selection
    st.subheader("🎭 Pilih Persona")
    persona_choice = st.selectbox(
        "Gaya Chatbot",
        options=list(PERSONAS.keys()),
        format_func=lambda x: f"{PERSONAS[x]['icon']} {PERSONAS[x]['name']}",
        index=list(PERSONAS.keys()).index(st.session_state.persona)
    )
    st.session_state.persona = persona_choice
    
    st.divider()
    
    # Temperature slider
    st.subheader("🌡️ Kreativitas")
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.temperature,
        step=0.1,
        help="Nilai lebih tinggi = lebih kreatif, nilai lebih rendah = lebih fokus"
    )
    st.session_state.temperature = temperature
    
    st.divider()
    
    # Statistics
    st.subheader("📊 Statistik")
    st.metric("Total Pesan", len(st.session_state.messages))
    st.metric("Percakapan", len([m for m in st.session_state.messages if m["role"] == "user"]))
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Hapus Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_session = None
        st.rerun()
    
    # Export chat
    if st.button("💾 Export Chat", use_container_width=True) and st.session_state.messages:
        chat_export = {
            "timestamp": datetime.now().isoformat(),
            "persona": st.session_state.persona,
            "messages": st.session_state.messages
        }
        st.download_button(
            label="Download JSON",
            data=json.dumps(chat_export, indent=2, ensure_ascii=False),
            file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

# Main content
st.title(f"{PERSONAS[st.session_state.persona]['icon']} Gemini AI Chatbot")
st.caption(f"Mode: {PERSONAS[st.session_state.persona]['name']} | Model: gemini-2.0-flash-exp")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ketik pesan Anda di sini..."):
    # Gunakan API key dari session state (sudah diisi default)
    api_key = st.session_state.api_key
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            
            # Initialize model with generation config
            generation_config = {
                "temperature": st.session_state.temperature,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
            
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-exp",
                generation_config=generation_config,
                system_instruction=PERSONAS[st.session_state.persona]['prompt']
            )
            
            # Create or get chat session
            if st.session_state.chat_session is None:
                st.session_state.chat_session = model.start_chat(history=[])
            
            # Send message and get streaming response
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Add assistant response to messages
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {str(e)}")
            st.info("💡 Pastikan API key valid dan Anda memiliki akses ke model gemini-2.0-flash-exp")

# Footer
st.divider()
st.caption("💡 Tip: Gunakan sidebar untuk mengubah persona dan tingkat kreativitas chatbot!")