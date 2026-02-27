import sqlite3

conn = sqlite3.connect('naskah.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS naskah (id INTEGER PRIMARY KEY AUTOINCREMENT, pertanyaan TEXT NOT NULL, jawaban TEXT NOT NULL)''')

data_naskah = [
    ("Bagaimana cara saya melakukan pembelian?", "Untuk melakukan pembelian, silakan pilih barang yang Anda minati dan klik 'Tambahkan ke Kartu Belanja'. Kemudian, lanjutkan ke Keranjang Belanja dan ikuti petunjuk untuk menyelesaikan pembelian Anda"),
    ("Bagaimana saya dapat mengetahui status pesanan saya?", "Anda dapat mengetahui status pesanan Anda dengan masuk ke akun Anda di situs web kami dan membuka bagian 'Pesanan Saya'. Di sana, Anda akan melihat status pesanan Anda saat ini"),
    ("Bagaimana saya bisa membatalkan pesanan?", "Jika Anda ingin membatalkan pesanan, silakan hubungi tim layanan pelanggan kami sesegera mungkin. Kami akan berusaha sebaik mungkin untuk membantu Anda membatalkan pesanan sebelum pesanan dikirim"),
    ("Apa yang harus saya lakukan jika pesanan tiba dalam keadaan rusak?", "Jika Anda menerima barang yang rusak, segera hubungi layanan pelanggan kami dan berikan foto kerusakannya. Kami akan membantu Anda menukar atau mengembalikan barang tersebut"),
    ("Bagaimana cara menghubungi dukungan teknis?", "Anda dapat menghubungi dukungan teknis kami dengan menghubungi nomor telepon yang tersedia di situs web kami. Atau, Anda dapat menghubungi kami melalui chatbot kami"),
    ("Bisakah saya mengubah metode pengiriman selama pembayaran?", "Ya. Anda dapat mengubah informasi pengiriman di halaman pembayaran. Metode pengiriman dan ketentuan yang tersedia akan dicantumkan di sana")
]

cursor.executemany('INSERT INTO naskah (pertanyaan, jawaban) VALUES (?, ?)', data_naskah)
conn.commit()
conn.close()
print("naskah.db SUDAH SIAP!")