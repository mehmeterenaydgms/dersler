#fonksiyon

"""def enBasitFonksiyon():
    print("En basit fonksiyonum çalıştırıldı")

enBasitFonksiyon()

def birazDahaZorFonksiyon():
    x = 5
    x = x + 1
    print(f"x'in güncel değeri '{x}'")
    
birazDahaZorFonksiyon()"""

"""def merhabaDe(merhabaDenilcekKisi):
    print(f"Merhaba {merhabaDenilcekKisi}")
    
merhabaDe("eren")"""

#zorunlu olarak girdi almayıp kullanıcının isteğine bırakıyoruz
"""def alternatifMerhaba(isim = "Python"):
    print(f"Merhaba {isim}")

alternatifMerhaba()    """

#Kaç argüman olduğunu blelirtmeden toplama işlemi yapma, args kullanımı
"""def sonsuzToplama(*args):
    return sum(args)

sonuc = sonsuzToplama(1, 2, 53, 234, 5234)
print(sonuc)"""

#kwargs kullanımı, fonksiyon ile sözlük oluşturma
"""
def kwargKullanimi(**kwargs):
    return(kwargs)

sonuc1 = kwargKullanimi(muz = 234, elma = 145, sakız = 2)
print(sonuc1)
print(type(sonuc1))"""


def controlKeyWord(**kwargs):
    if "python" in kwargs:
        print("Python anahtar kelimeler içerisinde yer alıyor")
    else:
        print("Python anahtar kelimeler arasında yer almıyor!")

sonuc2 = controlKeyWord(java = 4, python = 10, c = 10, assembly = 1)
print(sonuc2)