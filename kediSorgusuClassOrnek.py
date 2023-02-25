#örnek 1
class Kedi():
    def __init__(self, turu, yasi, cinsiyeti):
        self.turu = turu
        self.yasi = yasi
        self.cinsiyeti = cinsiyeti
    
    def kedininYasiKac(self):
        return f"Kedinin yaşı :{self.yasi}"
        
    def kedininTuruNe(self):
        return f"Kedinin türü :{self.turu}"
        
    def kedininCinsiyetiNe(self):
        return f"Kedinin cinsiyeti :{self.cinsiyeti}"
        
        
hera = Kedi("British", 1, "Dişi")

kediSorgu = input("Hangi kedi ile ilgili bilgi almak istiyorsunuz :")

if kediSorgu == "hera" or kediSorgu == "Hera":
    print(hera.kedininTuruNe())
    print(hera.kedininYasiKac())
    print(hera.kedininCinsiyetiNe())
else:
    print("Böyle bir kedi petshopumuzda bulunmamaktadır")