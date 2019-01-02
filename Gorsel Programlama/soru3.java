abstract class Medya{
    String cikisYili;
    String medyaBasligi;
    int satisAdeti;

    public abstract void isim(String isim)
    public abstract void yil(String yil)
    public abstract void adet(int adet)
}
class Muzik extends Medya{

    @Override
    public void isim(String isim) {
        medyaBasligi = isim;
        nesneBilgileriniYaz();
    }

    @Override
    public void yil(String yil) {
        cikisYili = yil;
        nesneBilgileriniYaz();
    }

    @Override
    public void adet(int adet) {
        satisAdeti = adet;
        nesneBilgileriniYaz();
    }
    public void nesneBilgileriniYaz(){
        System.out.println( "Medya Başlığı : " + medyaBasligi
                + "\nCıkış Yılı : " + cikisYili
                + "\nSatış Adeti : " + satisAdeti);
    }
}
class Film extends Medya{

    @Override
    public void isim(String isim) {
        medyaBasligi = isim;
        nesneBilgileriniYaz();
    }

    @Override
    public void yil(String yil) {
        cikisYili = yil;
        nesneBilgileriniYaz();
    }

    @Override
    public void adet(int adet) {
        satisAdeti = adet;
        nesneBilgileriniYaz();
    }

    public void nesneBilgileriniYaz(){
        System.out.println( "Medya Başlığı : " + medyaBasligi
                + "\nCıkış Yılı : " + cikisYili
                + "\nSatış Adeti : " + satisAdeti);
    }
}