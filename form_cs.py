import streamlit as st

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

jumlah_list = [str(i) for i in range(1, 11)]

# Inisialisasi session state
if 'daftar_pesanan' not in st.session_state:
    st.session_state.daftar_pesanan = []
if 'last_combo' not in st.session_state:
    st.session_state.last_combo = ""

# Input Data Customer
st.subheader("🧾 Data Customer")
nama = st.text_input("📌 Nama Lengkap")
alamat = st.text_area("🏠 Alamat Lengkap (RT/RW, Kel, Kec, Kota, Kode Pos)")
no_hp = st.text_input("📱 No HP yang aktif")
pembayaran = st.radio("💳 Metode Pembayaran", ["COD", "Transfer Bank"])

# Tambah Produk setelah input no HP
st.subheader("🛒 Pilih Produk & Jumlah")
col1, col2 = st.columns(2)
with col1:
    produk_dipilih = st.selectbox("Pilih Produk", ["-"] + produk_list, key="produk")
with col2:
    jumlah_dipilih = st.selectbox("Jumlah (pcs)", ["-"] + jumlah_list, key="jumlah")

# Auto-tambah jika kombinasi valid dan berbeda dari sebelumnya
if produk_dipilih != "-" and jumlah_dipilih != "-":
    combo = f"{produk_dipilih} x {jumlah_dipilih} Pcs"
    if combo != st.session_state.last_combo:
        st.session_state.daftar_pesanan.append(combo)
        st.session_state.last_combo = combo
        st.session_state.produk = "-"
        st.session_state.jumlah = "-"
        st.experimental_rerun()

# Tampilkan daftar pesanan
if st.session_state.daftar_pesanan:
    st.markdown("### 📋 Daftar Produk yang Dipesan:")
    for i, item in enumerate(st.session_state.daftar_pesanan):
        col1, col2 = st.columns([9, 1])
        with col1:
            st.write(f"{i+1}. {item}")
        with col2:
            if st.button("❌", key=f"hapus_{i}"):
                st.session_state.daftar_pesanan.pop(i)
                st.session_state.last_combo = ""
                st.experimental_rerun()

# Generate message
if st.button("Generate Pesan WhatsApp"):
    if not all([nama, alamat, no_hp, st.session_state.daftar_pesanan, pembayaran]):
        st.warning("Harap isi semua kolom terlebih dahulu.")
    else:
        produk_text = "\n".join([f"- {item}" for item in st.session_state.daftar_pesanan])

        pesan = f"""
📌 Nama Lengkap: {nama}
🏠 Alamat Lengkap: {alamat}
📱 No HP yang aktif: {no_hp}
👖 Produk yang dipesan:\n{produk_text}
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
