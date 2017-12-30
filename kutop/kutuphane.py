import sqlite3
import time
import random


class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski,idno):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        self.idno = idno

    def __str__(self):

        return "\nKitap İsmi : {}\nYazar : {}\nYayınevi : {}\nTür : {}\nBaskı : {}\nID : {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski,self.idno)


class Kutuphane():

    def __init__(self):

        self.baglanti_olustur()


    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("veritabani2.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT,id INT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):

        self.baglanti.close()




    def kitaplari_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar =  self.cursor.fetchall()

        if(len(kitaplar) == 0):

            print("Kütüphanede ekli bir kitap bulunmamaktadır.")

        else:

            print("**************************")
            print("******Bütün Kitaplar******")
            print("**************************\n")

            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5])

                print(kitap)
                print("--------------------------\n")

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar Where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):

            print("Böyle bir kitap bulunmamaktadır.")

        else:

            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][4])
            print(kitap)


    def kitap_ekle(self,kitap):

        sorgu = "Insert into kitaplar values(?,?,?,?,?,?)"
        #zaxd = self.id_ekleme(kitap.isim)
        sayi = 1001
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski,kitap.idno))


        self.baglanti.commit()


    def kitap_sil(self,isim):


        sorgu = "Delete from kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baski_yukselt(self,isim):

        sorgu="Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmamaktadır")

        else:

            baski = kitaplar[0][4]

            baski += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baski,isim,))

            self.baglanti.commit()

    def bulma(self,kitap):

        sorgu = "Select id From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(kitap,))
        deger = self.cursor.fetchmany(1)

        return deger





