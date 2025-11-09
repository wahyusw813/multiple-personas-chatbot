# ✨ Multiple Personas Chatbot

<div align="center">

![Gemini AI](https://img.shields.io/badge/Google-Gemini%202.0-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Chatbot AI yang powerful dengan berbagai persona, ditenagai oleh Google Gemini 2.0 Flash**

[🚀 Demo Live](https://multiple-personas-chatbot.streamlit.app/) • [Dokumentasi](#fitur-utama) • [Instalasi](#-instalasi)

---

### 🎮 Try it Now!

<a href="https://multiple-personas-chatbot.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-Click_Here!-FF4B4B?style=for-the-badge&logoColor=white" alt="Live Demo"/>
</a>

**Coba langsung tanpa instalasi! Aplikasi sudah online dan siap digunakan.**

<img src="https://img.icons8.com/fluency/96/chatbot.png" alt="chatbot" width="120"/>

</div>

---

## 🌟 Tentang Project

Multiple Personas Chatbot adalah aplikasi chatbot interaktif yang dibangun menggunakan **Streamlit** dan **Google Gemini 2.0 Flash**. Aplikasi ini menawarkan pengalaman percakapan yang natural dengan berbagai persona yang dapat disesuaikan, streaming response real-time, dan antarmuka yang elegan.

> 🔗 **Live Demo:** [https://multiple-personas-chatbot.streamlit.app/](https://multiple-personas-chatbot.streamlit.app/)  
> Coba sekarang tanpa perlu install apapun!

### 🎯 Mengapa Project Ini?

- 🚀 **Cepat & Responsif** - Menggunakan Gemini 2.0 Flash, model AI tercepat dari Google
- 🎭 **Multi-Persona** - 4 gaya komunikasi berbeda sesuai kebutuhan
- 💾 **Export Chat** - Simpan riwayat percakapan Anda
- 🎨 **UI Modern** - Antarmuka dark mode yang nyaman di mata
- 🔒 **Aman** - API key tersimpan dengan aman
- 📊 **Statistik Real-time** - Pantau aktivitas percakapan Anda

---

## ✨ Fitur Utama

### 🎭 **4 Persona Berbeda**

| Persona | Deskripsi | Cocok Untuk |
|---------|-----------|-------------|
| 🤝 **Asisten Ramah** | Hangat dan membantu | Pertanyaan umum, casual chat |
| 💼 **Profesional** | Formal dan terstruktur | Konsultasi bisnis, laporan |
| 🎨 **Kreatif** | Imajinatif dan unik | Brainstorming, storytelling |
| ⚙️ **Teknis** | Detail dan akurat | Programming, troubleshooting |

### 🎛️ **Kontrol Kreativitas**

Sesuaikan tingkat kreativitas response dengan slider temperature:
- **0.0 - 0.3**: Fokus dan konsisten
- **0.4 - 0.7**: Seimbang (default)
- **0.8 - 1.0**: Kreatif dan bervariasi

### 💬 **Streaming Response**

Response AI muncul secara real-time seperti sedang mengetik - memberikan pengalaman yang lebih natural dan engaging!

### 📊 **Statistik & Analytics**

Pantau aktivitas chatbot Anda:
- Total jumlah pesan
- Jumlah percakapan
- Export data dalam format JSON

---

## 🚀 Instalasi

### Prasyarat

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Google Gemini API Key ([Dapatkan di sini](https://aistudio.google.com/app/api-keys))

### Langkah Instalasi

1. **Clone repository**
```bash
git clone https://github.com/wahyusw813/multiple-personas-chatbot.git
cd multiple-personas-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup API Key**

Edit file `app.py`, cari baris berikut dan ganti dengan API key Anda:
```python
if "api_key" not in st.session_state:
    st.session_state.api_key = "YOUR_GEMINI_API_KEY_HERE"
```

4. **Jalankan aplikasi**
```bash
streamlit run multiplepersonas_app.py
```

5. **Buka browser**

Aplikasi akan terbuka otomatis di `http://localhost:8501`

---

## 📖 Cara Penggunaan

### Basic Usage

1. **Pilih Persona** - Pilih gaya komunikasi di sidebar
2. **Atur Kreativitas** - Sesuaikan slider temperature
3. **Mulai Chat** - Ketik pesan di input box dan tekan Enter
4. **Lihat Response** - AI akan merespon secara real-time

### Advanced Features

#### Export Chat History
```
1. Chat dengan AI seperti biasa
2. Klik tombol "💾 Export Chat" di sidebar
3. Download file JSON berisi riwayat lengkap
```

#### Reset Conversation
```
1. Klik tombol "🗑️ Hapus Riwayat Chat" di sidebar
2. Konfirmasi untuk memulai percakapan baru
```

---

## 🛠️ Teknologi yang Digunakan

<table>
  <tr>
    <td align="center" width="96">
      <img src="https://img.icons8.com/color/48/000000/google-logo.png" width="48" height="48" alt="Google" />
      <br>Gemini 2.0
    </td>
    <td align="center" width="96">
      <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="48" height="48" alt="Streamlit" />
      <br>Streamlit
    </td>
    <td align="center" width="96">
      <img src="https://img.icons8.com/color/48/000000/python.png" width="48" height="48" alt="Python" />
      <br>Python 3.8+
    </td>
    <td align="center" width="96">
      <img src="https://img.icons8.com/fluency/48/000000/json.png" width="48" height="48" alt="JSON" />
      <br>JSON
    </td>
  </tr>
</table>

### Dependencies

- `streamlit` - Web framework untuk aplikasi
- `google-generativeai` - SDK untuk Google Gemini API
- `json` - Handling data export
- `datetime` - Timestamp untuk export

---

## 📁 Struktur Project

```
multiple-personas-chatbot/
│
├── multiplepersonas_app.py   # Main application file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
---

## 🎨 Screenshots

### Main Chat Interface
```
┌─────────────────────────────────────────────────────┐
│  Multiple Personas Chatbot                          │
│  Mode: Asisten Ramah | Model: gemini-2.0-flash-exp  │
├─────────────────────────────────────────────────────┤
│                                                     │
│   User: Halo, apa kabar?                            │
│                                                     │
│   AI: Halo! Kabar saya baik, terima kasih...        │
│                                                     │
│  [Ketik pesan Anda di sini...]                      │
└─────────────────────────────────────────────────────┘
```

### Sidebar Settings
```
⚙️ Pengaturan Chatbot
─────────────────────
🎭 Pilih Persona
  → Asisten Ramah
  
🌡️ Kreativitas
  ●────────○ 0.7

📊 Statistik
  Total Pesan: 12
  Percakapan: 6

🗑️ [Hapus Riwayat Chat]
💾 [Export Chat]
```

---

## 🔐 Keamanan & Privacy

- ✅ API key tidak disimpan di database
- ✅ Riwayat chat hanya tersimpan di session browser
- ✅ Tidak ada data yang dikirim ke server eksternal selain Google Gemini API
- ✅ Export chat dalam format JSON untuk kontrol penuh atas data Anda

---

## 🚀 Deploy ke Cloud

### ✅ Already Deployed!

**Aplikasi ini sudah live di:** [https://multiple-personas-chatbot.streamlit.app/](https://multiple-personas-chatbot.streamlit.app/)

### Streamlit Cloud (Gratis)

Ingin deploy versi Anda sendiri?

1. Push code ke GitHub
2. Kunjungi [share.streamlit.io](https://share.streamlit.io)
3. Connect dengan GitHub repository
4. Deploy dengan satu klik!

**Tips Deploy:**
- Gunakan Streamlit Secrets untuk menyimpan API key dengan aman
- Pastikan `requirements.txt` sudah lengkap
- Branch default biasanya `main` atau `master`

---

## 📄 License

Project ini dilisensikan di bawah [MIT License](LICENSE) - lihat file LICENSE untuk detail lengkap.

---

## 👨‍💻 Author

**Wahyu Satrio Widodo**

- GitHub: [@wahyusw813](https://github.com/wahyusw813)
- LinkedIn: [Wahyu Satrio Widodo](https://linkedin.com/in/wahyu-satrio-widodo-4337612b4)
- Email: wahyuswidodo813@gmail.com

---

## 🙏 Acknowledgments

- [Google Gemini API](https://ai.google.dev/) - Untuk AI engine yang powerful
- [Streamlit](https://streamlit.io/) - Untuk framework yang mudah digunakan
- [Icons8](https://icons8.com/) - Untuk icon-icon yang keren
- Komunitas open-source yang luar biasa!

---

<div align="center">

### ⭐ Jika project ini membantu Anda, berikan star ya!

**Made with ❤️ and ☕ by Wahyu Satrio Widodo**

[⬆ Back to Top](#-gemini-ai-chatbot)

</div>
