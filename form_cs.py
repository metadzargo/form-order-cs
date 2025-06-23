import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Form CS WhatsApp", layout="centered")
st.title("📦 Form Input Order Pelanggan")

# Daftar produk
produk_list = [
    "ANKLE-HITAM-S28", "ANKLE-HITAM-M30", "ANKLE-HITAM-L32", "ANKLE-HITAM-XL34",
    "ANKLE-HITAM-XXL36", "ANKLE-HITAM-3XL38", "ANKLE-HITAM-4XL40",
    "ANKLE-DARKGREY-S28", "ANKLE-DARKGREY-M30", "ANKLE-DARKGREY-L32", "ANKLE-DARKGREY-XL34",
    "ANKLE-DARKGREY-XXL36", "ANKLE-DARKGREY-3XL38", "ANKLE-DARKGREY-4XL40",
    "ANKLE-LIGHTGREY-S28", "ANKLE-LIGHTGREY-M30", "ANKLE-LIGHTGREY-L32", "ANKLE-LIGHTGREY-XL34",
    "ANKLE-LIGHTGREY-XXL36", "ANKLE-LIGHTGREY-3XL38", "ANKLE-LIGHTGREY-4XL40",
    "ANKLE-MOCA-S28", "ANKLE-MOCA-M30", "ANKLE-MOCA-L32", "ANKLE-MOCA-XL34",
    "ANKLE-MOCA-XXL36", "ANKLE-MOCCA-3XL38", "ANKLE-MOCCA-4XL40",
    "ANKLE-PUTIH-S28", "ANKLE-PUTIH-M30", "ANKLE-PUTIH-L32", "ANKLE-PUTIH-XL34",
    "ANKLE-PUTIH-XXL36", "ANKLE-PUTIH-3XL38", "ANKLE-PUTIH-4XL40",
    "ANKLE-CREAM-S28", "ANKLE-CREAM-M30", "ANKLE-CREAM-L32", "ANKLE-CREAM-XL34",
    "ANKLE-CREAM-XXL36", "ANKLE-CREAM-3XL38", "ANKLE-CREAM-4XL40"
]

# Input Fields
nama = st.text_input("📌 Nama Lengkap")
alamat = st.text_area("🏠 Alamat Lengkap (RT/RW, Kel, Kec, Kota, Kode Pos)")
no_hp = st.text_input("📱 No HP yang aktif")
produk_terpilih = st.multiselect("👖 Produk yang dipesan (bisa lebih dari satu)", produk_list)
pembayaran = st.radio("💳 Metode Pembayaran", ["COD", "Transfer Bank"])

# Generate message
if st.button("Generate Pesan WhatsApp"):
    if not all([nama, alamat, no_hp, produk_terpilih, pembayaran]):
        st.warning("Harap isi semua kolom terlebih dahulu.")
    else:
        produk_text = "\n".join([f"- {p}" for p in produk_terpilih])
        produk_text = "\n" + produk_text  # Tambahkan newline di awal daftar

        pesan = f"""
📌 Nama Lengkap: {nama}
🏠 Alamat Lengkap: {alamat}
📱 No HP yang aktif: {no_hp}
👖 Produk yang dipesan:{produk_text}
💳 Metode Pembayaran: {pembayaran}

🕒 Catatan Penting:
Pesanan yang masuk atau transfer sebelum **jam 15.00 WIB**, akan kami kirim **hari ini juga** 🚚💨
"""

        if pembayaran == "Transfer Bank":
            pesan += "\nJika Kakak memilih **Transfer Bank**,\n"
            pesan += "jangan lupa untuk **lampirkan screenshot bukti transfernya**, lalu kirim ke aku (Meta) ya Kak 📸✅\n"
        else:
            pesan += "\nKalau COD, cukup kirim datanya saja, dan bayar saat barang sampai.\n"

        pesan += "\nSetelah Kakak isi, aku langsung bantu proses ya 😊"

        st.success("Pesan berhasil dibuat!")
        st.text_area("👇 Salin pesan ini", value=pesan.strip(), height=300)
        st.code(pesan.strip(), language='markdown')
