import math

# declarasi variable
no = []
judulBuku = []
harga_satuan = []
jml_Beli_buku = []
sub_total = []

def input_program():
    '''inputan awal program'''
    print("Toko Buku Cahya Ilmu")
    print("-"*46)
    print("kode\t Judul Buku\t\t Harga")
    print("-"*46)
    print("B001\t Pemrograman python\t Rp. 50.000")
    print("B001\t Dasar Data Science\t Rp. 75.000")
    print("B001\t Belajar laravel 10\t Rp. 60.000")
    print("B001\t Jaringan komputer\t Rp. 80.000")
    print("-"*46)
    
    no_transaksi = input("Nomor Transaksi : ")
    nama_pembeli = input("Nama Pembeli : ")
    jml_jenisBuku = int(input("Jumlah Jenis Buku yang Dibeli : "))
    
    # blok perulagan
    for i in range(1,jml_jenisBuku+1):
        print(f"Tiket ke-{i}")
        kode_input = input("Pilih Kode Buku [B001|B002|B003|B004] : ")
        jml_bukuBeli = int(input("Jumlah Buku yang Dibeli                : "))
        jml_Beli_buku.append(jml_bukuBeli)
        
        if kode_input == "B001":
            judul_buku = "Pemrograman Python"
            judulBuku.append(judul_buku)
            harga = 50000
            harga_satuan.append(harga)
            sub_total.append(harga*jml_bukuBeli)
        elif kode_input == "B002":
            judul_buku = "Dasar Data Science"
            judulBuku.append(judul_buku)
            harga = 75000
            harga_satuan.append(harga)
            sub_total.append(harga*jml_bukuBeli)
        elif kode_input == "B003":
            judul_buku = "Belajar Laravel 10"
            judulBuku.append(judul_buku)
            harga = 60000
            harga_satuan.append(harga)
            sub_total.append(harga*jml_bukuBeli)
        elif kode_input == "B004":
            judul_buku = "Jaringan Komputer"
            judulBuku.append(juduL_buku)
            harga = 80000
            harga_satuan.append(harga)
            sub_total.append(harga*jml_bukuBeli)
        
    return no_transaksi, nama_pembeli,  kode_input, jml_bukuBeli, i, jml_jenisBuku, sub_total

# main program
no_transaksi, nama, kode, jml_beli, no, jml_jenisBuku, sub_total = input_program()
total_bayar = sum(sub_total)

print()
print("Toko Buku Cahya Ilmu".center(46))
print(f"No. Nota : {no_transaksi}")
print(f"Pembeli  : {nama}")
print(f'''
-------------------------------------------------------
    no    Judul Buku            Harga    Jumlah  Sub
                                Satuan   Beli    Total
-------------------------------------------------------
    ''')

for i in range(jml_jenisBuku):
    print(f"     {i+1}    {judulBuku[i]}     {harga_satuan[i]}     {jml_Beli_buku[i]}    {sub_total[i]}")
    
print("-"*55)
print(f"                            Total Bayar    :  Rp.{total_bayar} ")
print()
print("** Terima kasih atas pembeliannya **".center(55))


