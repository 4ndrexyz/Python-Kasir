def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('Masukkan User     : ')
    password = input('Masukkan Password : ')
 
    if username == 'admin' and password == 'pass':
        print('Login Sukses !\n\n')
        main_menu()
    else:
        print('Login Gagal !')
        get_login()

def counter_kasir():
    counter = input('Mau menghitung ulang ? (y/n) : ')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('ingin hitung lagi..?')
        tanya()
     
    else:
        print('Input program salah !')

def kasir():
    # masukan input dari user
    nama_barang = input('Masukkan Pesanan   : ')
    harga = int(input('Masukkan Harga   : '))
    jumlah_beli = int(input('Masukkan Jumlah Barang yang Anda Beli   : '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'harga total: {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('masukan pembayaran: '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'Kembalian Anda Adalah : {kembalian}')
        tanya()
     
    elif bayar == total:
        print('Uang Anda Pas, Terimakasih :)')
 
    else:
        print(f'Maaf Uang Anda Tidak Cukup, Uang Anda Kurang {kurang}')
        counter_kasir()

        # membuat kalkulator
def kalkulator():
    print('=' * 10)
    print(' === Kalukator === ')
 
    print()
    print('Operator')
    print('=' * 10)
    print('1. Tambah')
    print('2. Kurang ')
    print('3. Pembagian')
    print('4. Perkalian')
    print('5. Modulus (Sisa Bagi)')
 
    a = int(input('Masukan bilangan pertama: '))
    b = int(input('Masukan bilangan ke dua: '))
 
    operator = input('Masukan Operator: ')
 
    if operator == '1':
        print('Hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('Hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('Hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('Hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('Hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('Harap Masukan Input yang Benar !')

def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'APLIKASI KASIR SEDERHANA', '=' * 10)
    print('Selamat Datang')
    print('=' * 20, 'Masukan Input Aplikasi', '=' * 20)
    print('1. Kasir')
    print('2. Kalkulator')
    print('3. Logout')
 
    # input pilihan
    pilihan = input('Pilih Menu: ')
 
    # pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('Program Keluar...')
        exit()
 
def tanya():
    tanya = input('Kembali ke Menu ? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('Input Salah')
        print('Masukan Input dengan Benar')


# membuat program kasir resto sederhana
def counter_kasir():
    counter = input('Hitung Lagi ? (y/n)  :')
    if counter == 'y':
         
        kasir()
     
    elif counter == 'n':
        print('Ingin Menghitung lagi ?')
        tanya()
     
    else:
        print('Input Program Salah Harap Ulangi')
 
def kasir():
    # masukan input dari user
    nama_barang = input('Masukan Pesanan Anda  : ')
    harga = int(input('Masukan Harga Barang  : '))
    jumlah_beli = int(input('Masukan Jumlah Barang yang Anda Beli  : '))
 
    # mengitung jumlah harga
    total = harga * jumlah_beli
     
    # cetak total harga
    print(f'Total Harga  : {nama_barang}, = {total}')
 
    # input pembayaran dari user
    bayar = int(input('Masukan Pembayaran  : '))
 
    # mengecek apakah pembayaran kurang atau ada kembalian
    kurang = total - bayar
    kembalian = bayar - total
 
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
     
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')
 
    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        counter_kasir()
 
 
def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'KASIR', '=' * 10)
    print('Selamat Datang')
    print('=' * 20, 'Masukan Input Aplikasi', '=' * 20)
    print('1. Kasir')
    print('2. Kalkulator')
    print('3. Logout')
 
    # input pilihan
    pilihan = input('pilih menu: ')
 
    # pilihan menu
    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('program exit')
        exit()
 
 
# membuat fungsi authentifikasi sederhana
def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
 
    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()
 
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')
 
# membuat kalkulator
def kalkulator():
    print('=' * 10)
    print('Program Kalukator')
 
    print()
    print('Operator')
    print('=' * 10)
    print('1. tambah')
    print('2. kurang ')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi/modulus')
 
    a = int(input('masukan bilangan pertama: '))
    b = int(input('masukan bilangan ke-dua: '))
 
    operator = input('masukan operator: ')
 
    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} adalah {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukan input yang benar sesuai menu diatas')
 
# main program
if __name__=='__main__':
    get_login()
