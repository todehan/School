
from kutuphane import *
#from ogrenci import *

print("""
             **********************************************************
             ****************KUTUPHANE UYGULAMASI**********************
             **********************************************************

             İşlemler :

             1. Kitapları Göster

             2. Kitap Sorgulama

             3. Kitap Ekle

             4. Kitap Sil

             5. Baskı Sayısı Yükseltme


             Çıkmak için 'q' tuşuna basınız.


             **********************************************************
             ****************KUTUPHANE UYGULAMASI**********************
             **********************************************************""")


kutuphane = Kutuphane()
#ogrenci = Ogrenci()

while True:

    islem = input("\nYapacağınız işlem : ")

    if(islem == "q"):
        print("Uygulama sonlandırılıyor...")
        break
    elif(islem == "1" ):

        kutuphane.kitaplari_goster()

    elif(islem == "2"):

        isim = input("Sorgulamak istediğiniz kitabın ismini giriniz : ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)

    elif(islem == "3"):

        isim = input("Kitabın ismini giriniz :")
        yazar = input("Yazarın ismini giriniz : ")
        yayinevi = input("Yayınevini giriniz : ")
        tur = input("Türünü giriniz : ")
        baski = int(input("Kaç adet baskı olduğunu giriniz : "))

        dosya= open('id.txt','r+')
        sayi = dosya.readline()

        sayi2=int(sayi)

        sayi2 +=1
        dosya.close()
        open('id.txt','w').close()
        dosya2 = open('id.txt','r+')
        dosya2.write(str(sayi2))
        dosya2.close()




        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski,sayi2)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap başarıyla eklendi.")

    elif(islem == "4"):

        isim = input("Kitabın ismini giriniz : ")

        cevap = input("Emin misiniz ? (E/H)")

        if(cevap == "E"):

            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap başarıyla silindi.")

    elif(islem == "5"):

        isim = input("Hangi kitabın baskı sayısını yükseltmek istiyorsunuz ? : ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı sayısı başarıyla yükseltildi")

    else:
        print("Geçersiz işlem...")




