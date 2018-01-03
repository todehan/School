        public static List<int> toplar = new List<int>();

        public static int p1 = 0, p2 = 0, p3 = 0, sayac = 52;

        public static bool kontrol = true;
        static void Main(string[] args)
        {

            olustur();
           
            Random ras = new Random();

           while(kontrol)
            {
                if (p1 > 21 && p2 > 21) { Console.WriteLine("İlk ve ikinci oyuncu elendi ! Kazanan üçüncü oyuncu"); kontrol = false; }
                else if (p3 > 21 && p2 > 21) { Console.WriteLine("İkinci ve Üçüncü oyuncu elendi ! Kazanan ilk oyuncu"); kontrol = false; }
                else if (p1 > 21 && p3 > 21) { Console.WriteLine("İlk ve üçüncü oyuncu elendi ! Kazanan ikinci oyuncu"); kontrol = false; }
                else
                {

                    for (int i = 1; i < 10; i++)
                    {
                        if (i == 4) break;

                        int sayi = ras.Next(0, 52);
                        hesapla(sayi, i);

                    }


                }


                
                

            }


            Console.ReadKey();
            

                       
        }

        public static void olustur()
        {
            
            for (int i = 1; i < 14; i++)
            {
                for (int j = 1; j < 5; j++)
                {
                    toplar.Add(i);
                }
            }

            toplar.Sort();

        }
        
        public static void hesapla(int deger,int kisi)
        {
            int s = 0;

            foreach (var i in toplar)
            {
                if (s == deger)
                {
                    if (kisi == 1) p1 += i;
                    if (kisi == 2) p2 += i;
                    if (kisi == 3) p3 += i;
                    toplar.RemoveAt(deger);
                    sayac--;
                    break;

                }
                else s++;
                
            }


            
        }
