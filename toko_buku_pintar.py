# Dictionary daftar karyawan
data_karyawan = {
    'cecep': 'cecep123',
    'udin': 'udin123',
    'asep': 'asep123',
    'maman': 'maman123'
}

# Dictionary daftar buku
daftar_buku_dic = {
    '1': "Buku Pemrograman Python",
    '2': "Buku Paket Matematika Kelas 7",
    '3': "Buku Paket Matematika Kelas 8",
    '4': "Buku Paket Matematika Kelas 9",
    '5': "Buku Paket IPA Kelas 7",
    '6': "Buku Paket IPA Kelas 8",
    '7': "Buku Paket IPA Kelas 9",
    '8': "Buku Paket B. Indonesia Kelas 7",
    '9': "Buku Paket B. Indonesia Kelas 8",
    '10': "Buku Paket B. Indonesia Kelas 9",
}

# Dictionary stok buku
daftar_stok_buku = {
    'Buku Pemrograman Python': 98,
    'Buku Paket Matematika Kelas 7': 48,
    'Buku Paket Matematika Kelas 8': 45,
    'Buku Paket Matematika Kelas 9': 42,
    'Buku Paket IPA Kelas 7': 32,
    'Buku Paket IPA Kelas 8': 76,
    'Buku Paket IPA Kelas 9': 11,
    'Buku Paket B. Indonesia Kelas 7': 99,
    'Buku Paket B. Indonesia Kelas 8': 65,
    'Buku Paket B. Indonesia Kelas 9': 79,
}

# Function untuk menampilkan stok buku
def stok_buku():
    print("|------------------------------------------------------------------------------------|")
    print("|    Nomor    |          Nama Buku           |       Harga       |       Stok        |")
    print("|------------------------------------------------------------------------------------|")
    
    for nomor, (judul, harga, stok) in enumerate(zip(daftar_buku_dic.values(), [63000, 99000, 99000, 99000, 87000, 87000, 87000, 50000, 50000, 50000], daftar_stok_buku.values()), 1):
        print(f"|      {nomor}      |    {judul.ljust(30)} |  Rp {harga:,.2f}  |        {stok}         ")
        print("|------------------------------------------------------------------------------------|")
        
    print("\t")

# Function untuk login
def login():
    print("\n|--------------------------------------------------------|")
    print("|            Selamat datang di toko buku pintar          |")
    print("|--------------------------------------------------------|")
    print("|                      Masuk Sebagai                     |")
    print("|                      1. Karyawan                       |")
    print("|                      2. Pembeli                        |")
    print("|                      3. Exit                           |")
    print("|--------------------------------------------------------|\n")
    
    masuk = int(input("Masuk Sebagai (1/2/3): "))
    
    if masuk == 1:
        username_karyawan = input("Masukkan nama anda: ")
        password_karyawan = input("Masukkan password anda: ")
        
        if username_karyawan in data_karyawan and data_karyawan[username_karyawan] == password_karyawan:
            print(f'Login Berhasil Sebagai {username_karyawan}')

            # Setelah login karyawan, berikan opsi lihat stok buku atau keluar
            print("\n|--------------------------------------------------------|")
            print("|                      Menu Karyawan                     |")
            print("|                      1. Lihat Stok Buku                |")
            print("|                      2. Keluar                         |")
            print("|--------------------------------------------------------|\n")

            pilihan_karyawan = int(input("Pilih Menu (1/2): "))

            if pilihan_karyawan == 1:
                stok_buku()
            elif pilihan_karyawan == 2:
                print("Terimakasih telah menggunakan layanan kami.")
                #break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

            # Karyawan keluar dari menu
        else:
            print('Login Tidak Berhasil. Silahkan coba lagi!')
            
    elif masuk == 2:
        username_pembeli = input("Masukkan nama anda: ")
        nomor_pembeli = input("Masukkan nomor telepon anda: ")
        print(f"Login Berhasil Sebagai {username_pembeli}")
        stok_buku()
        
        berapa_buku = int(input("Anda Ingin Membeli Berapa Buku: "))
        beli_buku(berapa_buku)

    elif masuk == 3:
        print("Terimakasih telah mengunjungi toko buku pintar")

    else:
        print("Pilihan tidak valid.")

# Function untuk proses pembelian
def beli_buku(jumlah_buku):
    buku_dibeli = []
    harga_buku = {}
    stok_terkini = daftar_stok_buku.copy()

    for i in range(jumlah_buku):
        nomor_buku = input(f"Masukkan Nomor Buku: ")
        
        if nomor_buku in daftar_buku_dic:
            judul_buku = daftar_buku_dic[nomor_buku]
            
            if stok_terkini[judul_buku] > 0:
                buku_dibeli.append(judul_buku)
                stok_terkini[judul_buku] -= 1
                harga_buku[judul_buku] = [63000, 99000, 99000, 99000, 87000, 87000, 87000, 50000, 50000, 50000][int(nomor_buku) - 1]
                print(f"{judul_buku} Ditambahkan Ke Keranjang. Stok Sekarang: {stok_terkini[judul_buku]}")
                
            else:
                print(f"Maaf, Stok buku {judul_buku} habis.")

        else:
            print("Buku Tidak Ada")

    # Proses pembelian
    if buku_dibeli:
        total_harga = sum(harga_buku[buku] for buku in buku_dibeli)
        print("\nStruk Pembelian:")
        print("Nama anda : Ahmad Diffa Jamaludin")
        print("Nomor Telepon Anda : 085717815076")
        print("|----------------------------------------------------------------------------------------|")
        print("|    No    |          Nama Buku           |       Harga       |       Jumlah        |")
        print("|----------------------------------------------------------------------------------------|")
        for nomor, buku in enumerate(buku_dibeli, 1):
            print(f"|   {nomor}   |    {buku.ljust(30)} |  Rp {harga_buku[buku]:,.2f}  |         1           |")
            print("|----------------------------------------------------------------------------------------|")

        print(f"\nTotal Harga: Rp {total_harga:,.2f}")

        uang_dibayar = float(input("Masukkan uang pembayaran: Rp "))
        if uang_dibayar < total_harga:
            print("Uang yang Anda masukkan kurang. Pembelian dibatalkan.")
        else:
            kembalian = uang_dibayar - total_harga
            print(f"Kembalian: Rp {kembalian:,.2f}")
            print("Terimakasih telah berbelanja di toko buku pintar")
            print("Ditunggu kedatangan selanjutnya ya")
    else:
        print("Tidak ada buku yang dibeli.")

# Program utama
login()
# stok_buku()

# berapa_buku = int(input("Anda Ingin Membeli Berapa Buku : "))
# beli_buku(berapa_buku)