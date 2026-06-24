import csv
FILE = "pajak.csv"

def baca_data():
    data = []

    try:  # ---> untuk mengecek file 'pajak.csv', jika ada lanjut baca data
            with open(FILE, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)

    except FileNotFoundError:
            print("\nData UMKM Belum ter isi") # ---> jika file  'pajak.csv' tidak ada data maka munculkan 'File Belum ter isi'
            print("Silahkan Isi Data terlebih dahulu") 
            pass
    
    return data

def tambah_umkm(data):
     umkm = {
          "id":input("ID UMKM : "),
          "nama toko":input("Nama Toko : "),
          "pemilik":input("Nama Pemilik : "),
          "omset":float(input("Omset : ")),
     }
     batas = 500.000000
     if umkm["omset"] >= batas:         
        umkm["pajak"] = umkm["omset"] * 0.05


     else:
          umkm["pajak"] = 0
          
     data.append(umkm)
     simpan_umkm(data)
     print("Data Berhasil Di tambahkan")

def simpan_umkm(data):
    with open(FILE, "w", newline="") as file: # ---> 'open()'= membuka file, "w"= tulis ulang data, 'newline'= mengisi baris kosong
        fieldnames = ["id", "nama toko", "pemilik", "omset", "pajak"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() # ---> untuk menulis header : id,pemilik,omset,pajak
        writer.writerows(data) # ---> untuk menulis semua data


def tampilkan_umkm(data):
    print("\n===== DATA UMKM =====")
    print()
    print(f"{'ID':<10} {'Nama Toko':<35} {'Pemilik':<20}{'Omset':}{'pajak':.1f}") # --> {'..':<10} = untuk menatur posisi rata kiri jarak 10 huruf
    print("-" * 85)

    for pajak in data:
            print(
                f"{pajak['id']:<10} "
                f"{pajak['nama toko']:<35} "
                f"{pajak['pemilik']:<20} "
                f"Rp.{float(pajak['omset']):.2f}"
                f"Rp.{float(pajak['pajak']):.2f}"
            )


def cari_umkm(data):
     global umkm
     id = input("Masukan ID UMKM : ")
     ditemukan = False

     for umkm in data:
          if umkm["id"] == id:
               print("\nData di Temukan ")
               print(f"ID : {umkm["id"]}")
               print(f"Nama Toko : {umkm["nama toko"]}")
               print(f"Pemilik : {umkm["pemilik"]}")
               print(f"Omset : Rp.{umkm["omset"]}")
               print(f"Pajak : Rp.{umkm["pajak"]}")

               ditemukan = True
               break
          else:
               print("Data Tidak di Temukan")


def sorting_omset(data):
     for i in range(len(data)):
          idx = i
          for j in range(i + 1, len(data)):
               
               if int(data[j]["omset"]) > int(data[idx]["omset"]):
                    idx = j

          data[i], data[idx] = data[idx], data[i]

          tampilkan_umkm(data)
    

def hapus_umkm(data):
     hapus_id = input("Masukan ID UMKM yang igin di hapus : ")
     ditemukan = False
     for umkm in data:
          if umkm["id"] == hapus_id:
               print("\nData Di temukan")
               print(f"Nama Toko : {umkm["nama toko"]}")

               confirm = input("Yakin ingin menghapus (y/n)? : ")
               if confirm == 'y':
                data.remove(umkm)
                simpan_umkm(data)


def menu():
    while True:
        print("""
╔══════════════════════════════════════════════════╗
║             SISTEM PERPAJAKAN UMKM               ║
║                 PPh Final 0.5%                   ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║  [1]  Tambah Data UMKM                           ║
║  [2]  Lihat Semua Data                           ║
║  [3]  Cari Data                                  ║
║  [4]  Sorting Omset & Pajak                      ║
║  [5]  Hapus Data UMKM                            ║
║  [0]  keluar                                     ║
║                                                  ║ 
║                                                  ║
╚══════════════════════════════════════════════════╝""")

        pilihan = input("  Pilih menu: ").strip()

        confirm = {
            "1": tambah_umkm,
            "2": tampilkan_umkm,
            "3": cari_umkm,
            "4": sorting_omset,
            "5": hapus_umkm,
        }

        if pilihan == "0":
            print("\n  Terima kasih. Program selesai.\n")
            break

        elif pilihan in confirm:
            data = baca_data()
            confirm[pilihan](data)
        else:
            print("\n  [!] Pilihan tidak valid. Coba lagi.")
            input("  Tekan Enter untuk melanjutkan...")
menu()

