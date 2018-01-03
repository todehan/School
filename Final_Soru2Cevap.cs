            int[] per = new int[4];

            int[] tutar = new int[4];



            int[] urun = new int[5];

            int[] adet = new int[5];

            int gelir = 0;



            Random ras = new Random();

            for (int i = 0; i < 4; i++)
            {
                per[i] = i + 1; tutar[i] = 0;
               
            }


            for(int i = 0; i<5;i++)
            {
                

                urun[i] = i + 1;
                adet[i] = 0;

            }

            for(int i = 0;i<30;i++)
            {
                for (int k = 0; k < 4; k++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        int sayi = ras.Next(1, 16);
                        tutar[k] = sayi * urun[j] * 3;
                        adet[j] += sayi;
                        gelir += tutar[k];

                    }
                }
            }


            for (int i = 0; i < 5; i++)
            {
                if (i <= 3) Console.WriteLine("{0}. personelin satış tutarı = {1} \n",per[i],tutar[i]);

                Console.WriteLine("{0}. üründen satılan toplam adet = {1}\n",urun[i],adet[i]);

                
                    
            }

            Console.WriteLine("Toplam Gelir = {0}",gelir);
