print("Selamat datang di kalkulator sederhana!")

def kecepatan():
    jarak = int(input("Masukkan jarak (meter)= "))
    waktu = int(input("Masukkan waktu (sekon)= "))
    kecepatan = jarak * waktu 
    print(f"kecepatannya adalah: {kecepatan}m/s")
    
def luas_persegi_panjang():
    panjang = int(input("Masukkan panjang persegi panjang = "))
    lebar = int(input("Masukkan lebar persegi panjang = "))
    luas = panjang * lebar
    print(f"luas persegi panjang adalah: {luas} m")
    
def kalkulator():
    n1 = int(input("Masukkan bilangan bulat pertama = "))
    operator = input("Masukkan operator (+, -, *, //) = ")
    n2 = int(input("Masukkan bilangan bulat kedua = "))
   
    if operator == '+':
        hasil = n1 + n2
        print(f'hasil dari penjumlahan adalah: {hasil}')
    elif operator == '-':
        hasil = n1 - n2
        print(f'hasil dari pengurangan adalah: {hasil}')
    elif operator == '*':
        hasil = n1 * n2
        print(f'hasil dari perkalian adalah: {hasil}')
    elif operator == '//':
        hasil = n1 // n2
        print(f"hasil dari pembagian adalah: {hasil}")
    else:
        print('operator tidak valid')


def luas_segitiga():
    alas = float(input('masukkan alas : '))
    tinggi = float(input('masukkan tinggi : '))
    luas = 0.5 * (alas * tinggi)
    print(f'luas segitiga adalah: {luas}')
    

def lingkaran():
    jari_jari = float(input('masukkan jari-jari lingkaran : '))
    luas_lingkaran = 3.14 * jari_jari**2
    print(f'luas lingkaran adalah: {luas_lingkaran}')
    
def jajar_genjang():
    alas = int(input("Masukkan alas = "))
    tinggi = int(input("Masukkan tinggi = "))
    luas_jajar_genjang = alas * tinggi 
    print(f'Luas jajar genjang adalah: {luas_jajar_genjang}')

def layang_layang():
    diagonal1 = float(input("Masukkan diagonal 1 = "))
    diagonal2 = float(input("Masukkan diagonal 2 = "))
    luas_layang_layang = float(diagonal1 * diagonal2) * 0.5
    print(f'Luas layang-layang adalah: {luas_layang_layang}') 
    
def volume_balok():
    panjang = int(input("Masukkan Panjang Balok = "))
    lebar = int(input("Masukkan Lebar Balok = "))
    tinggi = int(input("Masukkan Tinggi Balok = "))
    volume = int(panjang * lebar * tinggi)
    print(f'Volume balok adalah: {volume}')
    
while True:
    pilih = int(input(f"""Pilihan:
    1. Kecepatan 
    2.Luas persegi panjang 
    3.Kalkulator 
    4.Luas segitiga 
    5.Lingkaran
    6.Luas jajar genjang
    7.Luas Layang-layang/belah ketupat
    8.Volume Balok
    9.exit/keluar
    pilih : """))
    
    if(pilih == 1):
       kecepatan()
    elif(pilih == 2):
        luas_persegi_panjang()
    elif(pilih == 3):
        kalkulator()
    elif(pilih == 4):
       luas_segitiga()
    elif (pilih == 5):
        lingkaran()
    elif (pilih == 6):
        jajar_genjang()
    elif (pilih == 7):
        layang_layang()
    elif (pilih == 8):
        volume_balok()
    elif (pilih == 9): 
        print('Terima kasih telah menggunakan program kami')  
        break
    else:
        print("input yang dimasukkan salah, ulangi")
