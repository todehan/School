interface KendiniTanit{
    public void isimYaz();
}
interface KendiniDetayliTanit extends KendiniTanit {
    void numaraniYaz();
    void SoyadiniYaz();
}
interface  Maast{
    void maasHesapla();
}

class Kisi implements KendiniDetayliTanit,Maast{
    String isim;
    String soyisim;
    String numara ;
    double tabanMaas;
    double maasKatsayi;

    public Kisi(double maasKatsayim,String ismim,String soyisimim,String numaram){
        isim = ismim;
        soyisim = soyisimim;
        numara= numaram;
        maasKatsayi = maasKatsayim;
    }
    @Override
    public void isimYaz() {

    }

    @Override
    public void numaraniYaz() {

    }

    @Override
    public void SoyadiniYaz() {

    }

    @Override
    public void maasHesapla() {

    }
    public void tumBilgileriDok(){

    }
}
class GenelMudur extends Kisi{

    public GenelMudur(String ismim, String soyisimim, String numaram) {
        super(1.0, ismim, soyisimim, numaram);
    }
}
class Mudur extends Kisi{

    public Mudur(String ismim, String soyisimim, String numaram) {
        super(1.0, ismim, soyisimim, numaram);
    }
}
class Muhendis extends Kisi{

    public Muhendis(String ismim, String soyisimim, String numaram) {
        super(1.0, ismim, soyisimim, numaram);
    }
}