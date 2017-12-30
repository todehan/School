import random


class uygulama():


    def __init__(self):

        self.hesapla=[2.90,3.50,5.50,9.90,7.70]
        self.toptanci=[0,0,0]
        self.toplamgelir=0
        self.aysatis=0
        self.satis=[0,0,0,0,0]

    def hesaplar(self):

         for i in range(0,30):
             ras = random.randrange(0,3)
             for j in range(0,5):
                 urun=random.randrange(51,323)
                 print(i+1,". gün ",j+1,". üründen ",urun," kadar satıldı.")
                 self.satis[j]+=(self.hesapla[j]*0.10)*urun
                 self.toplamgelir+=(self.hesapla[j]*urun)-((self.hesapla[j]*0.10)*urun)
                 self.aysatis+=urun
                 if(ras==0):
                     self.toptanci[0]+=self.satis[j]
                 if(ras==1):
                     self.toptanci[1]+=self.satis[j]
                 if(ras==2):
                     self.toptanci[2]+=self.satis[j]
             print("\n")


    def goster(self):


        self.hesaplar()
        print("---------------------------------")
        print("Aylık satına ürün sayısı: ",self.aysatis)
        print("Toplam gelir : ",self.toplamgelir)
        print("1. toptancıya ödenen toplam tutar: ", self.toptanci[0])
        print("2. toptancıya ödenen toplam tutar: ", self.toptanci[1])
        print("3. toptancıya ödenen toplam tutar: ", self.toptanci[2])
