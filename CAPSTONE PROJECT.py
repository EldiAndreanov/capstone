from prettytable import PrettyTable

mobil_list = [
    {"plat_no":"B 2010 EA","merk": "Avanza", "stock": "tersedia", "harga": 150000},
    {"plat_no":"B 1075 BA","merk": "Xenia", "stock": "tersedia", "harga": 100000},
    {"plat_no":"B 9150 QK","merk": "Innova", "stock": "tersedia", "harga": 250000},
]

def tampilkan_tabel():
    tabel = PrettyTable()
    tabel.field_names = ["No","Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"] #show data menggunakan prettytable dengan nama kolom tersebut
    
    for index, mobil in enumerate(mobil_list): 
        tabel.add_row([index+1, mobil["plat_no"],mobil["merk"], mobil["stock"], mobil["harga"]]) #perulangan untuk show data pada list, untuk membuat tabel
    
    print(tabel)

def tabel_tersedia():
    tabel = PrettyTable()
    tabel.field_names = ["No","Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"] #show data menggunakan prettytable dengan nama kolom tersebut

    mobil_list_sorted = sorted(mobil_list, key=lambda x: x["stock"] == "tidak tersedia")

    for index, mobil in enumerate(mobil_list_sorted):
        if mobil ["stock"].lower() == 'tersedia':
            tabel.add_row([index+1, mobil["plat_no"],mobil["merk"], mobil["stock"], mobil["harga"]]) #perulangan untuk show data pada list, untuk membuat tabel
    
    print(tabel)

def tabel_harga_minimal():
    tabel = PrettyTable()
    tabel.field_names = ["No","Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"] #show data menggunakan prettytable dengan nama kolom tersebut

    while True:
        try:
            harga_maksimal = int(input('Masukan harga maksimal yang ingin ditampilkan: '))
            if harga_maksimal <= 0:
                print("Harga maksimal harus lebih besar dari 0.\n")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


    for index, mobil in enumerate(mobil_list):
        if mobil ["harga"] <= harga_maksimal:
            tabel.add_row([index+1, mobil["plat_no"],mobil["merk"], mobil["stock"], mobil["harga"]]) #perulangan untuk show data pada list, untuk membuat tabel
    
    print(tabel)

def tabel():
    while True:
        print('\nMenu')
        print('1. Tampilkan semua data mobil')
        print('2. Tampilkan data mobil yang tersedia')
        print('3. Tampilkan data mobil berdasarkan harga max')
        print('4. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-4: ')

        if angka == '1':
            tampilkan_tabel()
        elif angka == '2':
            tabel_tersedia()
        elif angka == '3':
            tabel_harga_minimal()
        elif angka == '4':
            break
        else :
            print('\nUlangi dengan memasukan angka 1-4')

def tambah_mobil(plat_no, merk, harga):
    global mobil_list

    for mobil in mobil_list:
        if mobil["plat_no"].lower() == plat_no.lower(): #Checker, jika ada nama yang sama maka akan muncul kalimat "sudah ada"
            print(f'\n{plat_no} sudah ada, tolong cek kembali')
            return
    plat_besar = plat_no.upper() #Membuat nama yang dimasukan menjadi kapital

    mobil_list.append({"plat_no": plat_besar, "merk": merk.title(), "stock": "tersedia", "harga": harga})
    
    print(f'\n{merk.title()} dengan plat nomer {plat_besar} berhasil ditambahkan.')

    tampilkan_tabel()

def hapus_mobil(no_plat):
    global mobil_list
    for mobil in mobil_list:
        if mobil["plat_no"].lower() == no_plat.lower(): #mencari 'nama' yang sudah diinputkan dalam sebuah perulangan
            x = input('Apakah kamu yakin untuk menghapus data?(Y/N) ')
            if x.upper() == 'Y' :
                mobil_list.remove(mobil)  # melakukan tindakan penghapusan data/list
                print(f"\nMobil dengan plat nomer {no_plat} berhasil dihapus.")
            return
    print(f"\nMobil {no_plat} tidak ditemukan.")

def pinjam_mobil():

    tabel_tersedia()

    mobil_list_sorted = sorted(mobil_list, key=lambda x: x["stock"] == "tidak tersedia")

    merk = input('\nMasukkan merk mobil yang ingin dirental: ')
    
    while True:
        try:
            jml_hari = int(input('Masukan jumlah hari anda akan merental mobil: '))
            if jml_hari <= 0:
                print("Jumlah hari harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    
    for mobil in mobil_list_sorted:
        if mobil['merk'].lower()== merk.lower() :
            if mobil['stock'] == 'tersedia' :
                ttl_harga = mobil['harga'] * jml_hari

                mobil["stock"] = 'tidak tersedia' #mengubah stock

                print(f"\n{mobil['merk'].upper()} dengan nopol {mobil['plat_no']} : {jml_hari} x {mobil['harga']} =  {ttl_harga}")

                
                print("Total : ", ttl_harga)

                uang_masuk = int(input("\nMasukan jumlah uang: "))

                while uang_masuk < ttl_harga :
                    print('\nKamu tidak dapat melanjutkan proses pembelian, karena:')
                    print("Uang kurang sebesar: ", ttl_harga-uang_masuk)
                    
                    uang_masuk = int(input("\nMasukan jumlah uang yang sesuai: "))

                if uang_masuk == ttl_harga :
                    print("\nTerimakasih sudah rental mobil")
                else :
                    print("\nTerimakasih sudah rental mobil")
                    print("Uang kembalian anda: ", uang_masuk-ttl_harga)    
                return
            print(f'\nMohon maaf, tidak ada mobil {merk.capitalize()} yang tersedia')

def kembali_mobil(no_plat):
    for mobil in mobil_list :
        if mobil['plat_no'].lower() == no_plat.lower() :
            if mobil['stock'] == 'tidak tersedia' :
                print(f'\nMobil {mobil["merk"].upper()} dengan plat nomor {no_plat.upper()} berhasil dikembalikan, Terimakasih')
                mobil["stock"] = "tersedia"
            else :
                print(f'\nMohon maaf, mungkin data yang anda masukan salah')

def rental_mobil():
    while True :
        print('\nMenu')
        print('1. Pinjam Mobil')
        print('2. Kembalikan Mobil')
        print('3. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-3: ')
        if angka == '1':
            pinjam_mobil()
        elif angka == '2':
            tampilkan_tabel()
            no_plat = input('Masukan no plat mobil yang ingin anda kembalikan: ')
            kembali_mobil(no_plat)
        elif angka == '3':
            break
        else :
            print('angka yang masukan salah, mohon gunakan angka antara 1-3.')

def main():
    while True:
        print('\nMenu:')
        print('1. Tampilkan Daftar Mobil')
        print('2. Tambah Mobil')
        print('3. Hapus Mobil')
        print('4. Rental Mobil')
        print('5. Keluar\n')
        
        angka = input('Ketikan pilihan anda (1-5): ')
        
        if angka == '1':
            tabel()
            
        elif angka == '2':
            plat_no = input('\nMasukkan plat nomer mobil: ')
            merk = input('Masukkan merk mobil: ')

            while True:
                try:
                    harga = int(input('Masukkan harga rental: '))
                    if harga <= 0:
                        print("Jumlah hari harus lebih besar dari 0.")
                        continue
                    break
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")

            tambah_mobil(plat_no, merk, harga)

        elif angka == '3':
            tampilkan_tabel()
            plat_no = input('\nMasukkan plat nomor mobil yang ingin dihapus: ')
            hapus_mobil(plat_no)

        elif angka == '4':
            rental_mobil()

        elif angka == '5':
            x = input('\nApakah kamu yakin untuk keluar dari halaman ini? (Y/N): ')
            if x.upper() == 'Y' :
                print('\nTerimakasih sudah berkunjung\n')
                break

        else:
            print('\nPilihan tidak ada, mohon coba kembali dengan angka 1-5.')

if __name__ == '__main__':
    main()