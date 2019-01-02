public class Soru4 {
    public static void main(){
        A a = new B();     
        B b = (B) new A(); 
                                    
    }

}
class A {
    int sayi1;
    void func1(){

    }
}
class B extends A{
    int sayi2;
    void func2() {

    }
}

/*


Upcasting : B sınıfı A sınıfından türetilidği için cast edilebilir.

Downcasting : Hata verir çünkü B sınıfında a sınıfında bulunmayan ifadeler vardır(sayi2, func2 ).

Cast işlemi yapıldığında b nesnesi A sınıfında B sınıfının ifadelerini arayacak ve bulamayacağı için hata verecektir.


*/