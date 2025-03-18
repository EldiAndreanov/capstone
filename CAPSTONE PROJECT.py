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

def tabel_no_plat():
    tabel = PrettyTable()
    tabel.field_names = ["No","Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"] #show data menggunakan prettytable dengan nama kolom tersebut

    no_plat = input('Masukan no plat yang ingin ditampilkan: ')
    found = False

    for index, mobil in enumerate(mobil_list):
        if mobil ["plat_no"].upper() == no_plat.upper():
            tabel.add_row([index+1, mobil["plat_no"],mobil["merk"], mobil["stock"], mobil["harga"]]) #perulangan untuk show data pada list, untuk membuat tabel
            
            found = True
    
    if found:
        print(tabel)
    else :
        print(f'\nMobil dengan no polisi {no_plat.upper()} tidak ditemukan.')

def tabel_tersedia():
    tabel = PrettyTable()
    tabel.field_names = ["No","Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"] #show data menggunakan prettytable dengan nama kolom tersebut

    mobil_list_sorted = sorted(mobil_list, key=lambda x: x["stock"] == "tidak tersedia")

    found = False

    for index, mobil in enumerate(mobil_list_sorted):
        if mobil ["stock"].lower() == 'tersedia':
            tabel.add_row([index+1, mobil["plat_no"],mobil["merk"], mobil["stock"], mobil["harga"]]) #perulangan untuk show data pada list, untuk membuat tabel
            found = True
    if found:
        print(tabel)
    else:
        print('Data yang kamu cari tidak ditemukan')


def opsi_satu():
    while True:
        print('\nMenu tampilkan data')
        print('1. Tampilkan semua data mobil')
        print('2. Tampilkan data mobil berdasarkan plat nomer')
        print('3. Tampilkan data mobil yang tersedia')
        print('4. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-4: ')

        if angka == '1':
            tampilkan_tabel()
        elif angka == '2':
            tabel_no_plat()
        elif angka == '3':
            tabel_tersedia()
        elif angka == '4':
            break
        else :
            print('\nUlangi dengan memasukan angka 1-4')

def tambah_mobil():
    global mobil_list
    plat_no = input('\nMasukkan plat nomer mobil: ')
    merk = input('Masukkan merk mobil: ')

    while True:
        try:
            harga = int(input('Masukkan harga rental: '))
            if harga <= 0:
                print("Jumlah harga harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    for mobil in mobil_list:
        if mobil["plat_no"].lower() == plat_no.lower(): #Checker, jika ada nama yang sama maka akan muncul kalimat "sudah ada"
            print(f'\nMobil dengan {plat_no.upper()} sudah ada, tolong cek kembali')
            return

    print(f'\nKamu menambahkan mobil dengan: \n plat nomer: {plat_no.upper()},\n mobil: {merk.capitalize()},\n harga: {harga}')
    setuju_simpan = input('Apakah anda yakin ingin menyimpan data mobil tersebut? (Y/N) ')
    
    if setuju_simpan.upper() == 'Y':
        mobil_list.append({"plat_no": plat_no.upper(), "merk": merk.title(), "stock": "tersedia", "harga": harga})
        
        print(f'\n{merk.title()} dengan plat nomer {plat_no.upper()} berhasil ditambahkan.')
    else :
        print('Anda tidak jadi menyimpan data')
    tampilkan_tabel()

def opsi_kedua():
    while True:
        print('\nMenu tambah data')
        print('1. Tambahkan data')
        print('2. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-2: ')

        if angka == '1':
            tambah_mobil()
        elif angka == '2':
            break
        else :
            print('ketikan angka yang sesuai (1/2)')

def ubah_data_mobil():
    tampilkan_tabel()

    tabel = PrettyTable()
    tabel.field_names = ["No", "Plat nomer", "Merk Mobil", "Ketersediaan", "Harga"]

    no_plat = input('Masukan no plat yang ingin diubah: ')
    found = False

    for index, mobil in enumerate(mobil_list):
        if mobil["plat_no"].upper() == no_plat.upper():
            tabel.add_row([index + 1, mobil["plat_no"], mobil["merk"], mobil["stock"], mobil["harga"]])
            found = True

    if found:
        print('\n', tabel)

        confirm_edit = input('Apakah kamu yakin ingin melanjutkan proses ubah data? (Y/N): ')
        while True:
            if confirm_edit.lower() == 'y':
                column_table = input('\nMasukan kolom yang ingin diubah: ')

                for mobil in mobil_list:
                    if mobil["plat_no"].lower() == no_plat.lower():
                        if column_table.lower() in ['merk mobil', 'merk']:
                            merk = input('Masukan merk mobil yang baru: ')
                            if confirm_action():
                                mobil["merk"] = merk.capitalize()
                                print('\nData berhasil di update')
                        elif column_table.lower() == 'ketersediaan':
                            tersedia = input('Masukan ketersediaan mobil (tersedia/tidak tersedia): ')
                            if tersedia.lower() in ['tersedia', 'tidak tersedia']:
                                if confirm_action():
                                    mobil["stock"] = tersedia.lower()
                                    print('\nData berhasil di update')
                            else:
                                print('\nAnda hanya bisa mengubah data dengan value tersedia/tidak tersedia')
                        elif column_table.lower() == 'harga':
                            try:
                                harga = int(input('Masukkan harga rental baru: '))
                                if harga <= 0:
                                    print("Jumlah harga harus lebih besar dari 0.")
                                else:
                                    if confirm_action():
                                        mobil["harga"] = harga
                                        print('\nData berhasil di update')
                            except ValueError:
                                print("Input tidak valid. Harap masukkan angka.")
                        else:
                            print(f'\nKolom {column_table} tidak ada dalam tabel ini')
                        break
                tampilkan_tabel()
                return
            elif confirm_edit.lower() == 'n':
                break
            else:
                print('\nValue yang kamu masukan tidak dikenali, tolong gunakan Y/N')
                confirm_edit = input('\nApakah kamu yakin ingin melanjutkan proses ubah data? (Y/N): ')
    else:
        print(f'\nMobil dengan no polisi {no_plat.upper()} tidak ditemukan.')

def confirm_action():
    while True:
        update = input('\nApakah anda yakin ingin mengubah data? (Y/N): ')
        if update.lower() == 'y':
            return True
        elif update.lower() == 'n':
            return False
        else:
            print('\nValue yang kamu masukan tidak dikenali, tolong gunakan Y/N')

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
                print('\nMohon maaf, mobil dengan nomor polisi tersebut masih tersedia')
            return
    print('\nMohon maaf, mobil dengan nomor polisi yang anda masukan tidak ada')
def opsi_ketiga():
    while True :
        print('\nMenu')
        print('1. Ubah data mobil')
        print('2. Pinjam Mobil')
        print('3. Kembalikan Mobil')
        print('4. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-4: ')
        if angka == '1':
            ubah_data_mobil()
        elif angka == '2':
            pinjam_mobil()
        elif angka == '3':
            tampilkan_tabel()

            no_plat = input('Masukan no plat mobil yang ingin anda kembalikan: ')
            kembali_mobil(no_plat)
        elif angka == '4':
            break
        else :
            print('angka yang masukan salah, mohon gunakan angka antara 1-4.')

def hapus_mobil(no_plat):
    global mobil_list

    for mobil in mobil_list:
        if mobil["plat_no"].lower() == no_plat.lower(): #mencari 'nama' yang sudah diinputkan dalam sebuah perulangan
            x = input('\nApakah kamu yakin untuk menghapus data?(Y/N) ')
            if x.upper() == 'Y' :
                mobil_list.remove(mobil)  # melakukan tindakan penghapusan data/list
                print(f"\nMobil dengan plat nomer {no_plat.upper()} berhasil dihapus.")
            return
    print(f"\nMobil dengan plat nomer {no_plat.upper()} tidak ditemukan.")

def opsi_keempat():
    while True:
        tampilkan_tabel()

        print('\nMenu tambah data')
        print('1. Hapus data mobil')
        print('2. Kembali ke menu utama\n')

        angka = input('Pilih angka 1-2: ')

        if angka == '1':
            plat_no = input('\nMasukkan plat nomor mobil yang ingin dihapus: ')
            hapus_mobil(plat_no)
        elif angka == '2':
            break
        else :
            print('ketikan angka yang sesuai (1/2)')


def main():
    while True:
        print('\nMenu:')
        print('1. Tampilkan Daftar Mobil')
        print('2. Tambah Mobil')
        print('3. Edit Data & Rental Mobil')
        print('4. Hapus Mobil')
        print('5. Keluar\n')
        
        angka = input('Ketikan pilihan anda (1-5): ')
        
        if angka == '1':
            opsi_satu()
            
        elif angka == '2':
            opsi_kedua()

        elif angka == '3':
            opsi_ketiga()

        elif angka == '4':
            opsi_keempat()

        elif angka == '5':
            x = input('\nApakah kamu yakin untuk keluar dari halaman ini? (Y/N): ')
            if x.upper() == 'Y' :
                print('\nTerimakasih sudah berkunjung\n')
                break

        else:
            print('\nPilihan tidak ada, mohon coba kembali dengan angka 1-5.')

if __name__ == '__main__':
    main()