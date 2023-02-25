benimListem = [10, 20, 30, 40, 50]
# for döngüsü ile bunların hepsini bir sayıya tek işlem ile döndürebiliriz
#for i in benimListem: #bu şekilded kullanılır
#    print(i / 5 * 6)

#Çıktı
"""12.0
24.0
36.0
48.0
60.0"""



"""for i in benimListem:
    yeniHesap = i / 5
    print(yeniHesap)"""

#Çıktı
"""
2.0
4.0
6.0
8.0
10.0"""


#Çift Sayıları Ekrana Yazdırır
myList = [10, 20, 673, 974, 27483, 8989, 12345, 765, 3214, 8967]

for i in myList:
    if (i % 2 == 0):
        print(i)