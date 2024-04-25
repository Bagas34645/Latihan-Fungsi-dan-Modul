import matematika
import menu

a=0
b=0

while(True):
    pilihan = menu.pilih_menu()

    if pilihan == '1':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = matematika.tambah(a, b)
        print("Hasil penambahan:", hasil)
    elif pilihan == '2':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = matematika.kurang(a, b)
        print("Hasil pengurangan:", hasil)
    elif pilihan == '3':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = matematika.kali(a, b)
        print("Hasil perkalian:", hasil)
    else:
        print("Pilihan tidak valid")
    
    apakah_selesai = input("Apakah Selesai (y/n)? ")
    if apakah_selesai == "y" or apakah_selesai == "Y":
        break
    
print("Program Berakhir, Terima Kasiih")

