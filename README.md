# Semua Bisa Kamu Beli
## Bagian-bagian Bot:
### Bot Discord untuk dukungan teknis (2)

Hai! Kami mewakili toko online bernama "Semua Bisa Kamu Beli"! Kami membutuhkan bot dukungan teknis yang akan menjawab Pertanyaan Umum dari pengguna, memberikan solusi untuk masalah, dan mengarahkan pertanyaan yang lebih rumit ke spesialis, jika diperlukan. Kami memiliki 2 departemen spesialis—programmer yang bisa memperbaiki masalah jika website atau pembayaran kami rusak, dan staf departemen penjualan yang menangani semua masalah produk.

Nilai proyek: 200 poin

Persyaratan:
1. Bot harus secara otomatis menjawab pertanyaan yang sering ditanyakan oleh pengguna kami. Kamu bisa menemukan FAQ di file ini.
2. Terapkan integrasi database—bot harus menyimpan semua pertanyaan yang harus diteruskan ke spesialis dalam tabel.
3. Bot harus bisa memproses pesan teks (akan lebih keren jika bot juga bisa menangani pesan suara, tapi itu opsional).
4. Bot harus menyediakan antarmuka yang jelas dan menarik untuk pelanggan.
5. Kami harap kamu menyediakan dokumentasi tentang cara menggunakan bot, ditujukan untuk admin toko.

## Bahasa Pemrograman:
- SQL
- Python

## Fitur:
Core Features (Sesuai Requirement)

### 🤖 Automatic FAQ Response
Bot secara otomatis menjawab pertanyaan umum berdasarkan sistem keyword matching.

### 🧠 Smart Department Classification
Bot dapat mengklasifikasikan pertanyaan ke:

### 💻 Programmer (masalah website / pembayaran)

### 🛒 Sales (masalah produk)

### 🗄 Database Integration (SQLite)
Semua pertanyaan kompleks disimpan ke dalam database.db dengan:

Username

Isi pesan

Departemen tujuan

### 🎛 Interactive Button Interface
Jika sistem tidak bisa mengklasifikasikan pertanyaan, user dapat memilih departemen melalui tombol interaktif.

### 📩 Ticket Management System
Admin dapat melihat semua tiket menggunakan command:

!lihat_tiket

### 💬 Text Message Processing
Bot dapat membaca dan memproses pesan teks secara real-time.


## Fitur tambahan:
### 🎨 Professional Embed UI
Semua jawaban menggunakan Discord Embed agar tampilan lebih bersih dan modern.
