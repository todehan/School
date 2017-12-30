import sqlite3

import time

class Ogr():

    def __init__(self,ogrno,isim,soyisim,sinif,kitap,tarih,idno):

        self.ogrno = ogrno
        self.isim = isim
        self.soyisim = soyisim
        self.sinif = sinif
        self.kitap = kitap
        self.tarih = tarih
        self.idno = idno

    def __str__(self):

        return "\nÖğrenci No : {}\nİsim : {}\nSoyisim : {}\nSınıf : {}\nKitap : {}\nTarih : {}\nID : {}\n".format(self.ogrno,self.isim,self.soyisim,self.sinif,self.kitap,self.tarih,self.idno)


class Ogrenci():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("veritabani2.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists ogrenciler(ogrno INT,isim TEXT,soyisim TEXT,sinif TEXT,kitap TEXT,tarih TEXT,idno INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):

        self.baglanti.close()

    def ogrenci_goster(self):

        sorgu = "Select * from ogrenciler"

        self.cursor.execute(sorgu)

        ogrenciler = self.cursor.fetchall()

        if(len(ogrenciler)==0):

            print("Herhangi bir öğrenci kaydı bulunmamaktadır...")

        else:

            print("*****************************")
            print("****** Öğrenci Listesi ******")
            print("*****************************\n")

            for i in ogrenciler:

                ogr = Ogr(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])

                print(ogr)
                print("--------------------------\n")


    def ogr_kitap_sorgula(self,kitap):

        sorgu = "Select * From ogrenciler Where kitap = ?"

        self.cursor.execute(sorgu,(kitap,))

        ogrkitap = self.cursor.fetchall()

        if(len(ogrkitap) == 0):

            print("Böyle bir kitap bulunmamaktadır.")

        else:



            ogr = Ogr(ogrkitap[0][0],ogrkitap[0][1],ogrkitap[0][2],ogrkitap[0][3],ogrkitap[0][4],ogrkitap[0][5])
            print(ogr)





    def ogr_kitap_ekle(self,kito):

        sorgu = "Insert into ogrenciler VALUES(?,?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(kito.ogrno,kito.isim,kito.soyisim,kito.sinif,kito.tarih,kito.id,))
        self.baglanti.commit()

    def ogr_sil(self,ogrno,kitap):

        sorgu = "Delete from ogrenciler where ogrno = ? AND kitap = ?"

        self.cursor.execute(sorgu,(ogrno,kitap,))
        self.baglanti.commit()






