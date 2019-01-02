public class Soru1 {
    public static void main(String[] args){
        Object[] obje = new Object[2];
        obje[0] = new AkilliTelefon();
        obje[1] = new Telefon();


        AkilliTelefon akTel1 = (AkilliTelefon) obje[0];
        AkilliTelefon akTel2 = (AkilliTelefon) obje[1];
        
        }
        }

class AkilliTelefon extends Telefon{

}

class Telefon{
    public void sesAc(){
        System.out.println("Ses açıldı");
    }
    public void sesKapat(){
        System.out.println("Ses kapatıldı");
    }
    public void sebekeAra(){
        System.out.println("Şebeke aranıyor ");
    }
}
