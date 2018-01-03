
        public delegate decimal Hesaplama(int sayi);
       
        static void Main(string[] args)
        {
            Random ras = new Random();

            for (int i = 0; i < 20; i++)
            {
                int deger = ras.Next(1,100);
                if (deger<=50)
                {
                    Hesaplama islem = Toplama;
                    islem(deger);
                }
                else
                {
                    Hesaplama islem = Carpma;
                    islem(deger);
                }
            }



            

        }
        static decimal Carpma(int sayi)
        {
            int carp = 1;
            return carp *= sayi;
        }

        static decimal Toplama(int sayi)
        {
            int topla = 0;
            return topla += sayi;
        }
