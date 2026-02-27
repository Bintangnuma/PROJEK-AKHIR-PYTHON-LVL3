import sqlite3

DB_NAME = "naskah.db"

def get_jawaban(id_naskah):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT jawaban FROM naskah WHERE id = ?", (id_naskah,))
    row = c.fetchone()

    conn.close()

    if row:
        return row[0]
    return "Jawaban tidak ditemukan."


def get_pembelian():
    return get_jawaban(1)

def get_status():
    return get_jawaban(2)

def get_batal():
    return get_jawaban(3)

def get_rusak():
    return get_jawaban(4)

def get_teknis():
    return get_jawaban(5)

def get_pengiriman():
    return get_jawaban(6)