#map
"""numaraListemiz = [10, 20, 30, 40, 50]

def ikiyleCarp(num):
    return num * 2

ikiyleCarpilmisListe = list(map(ikiyleCarp, numaraListemiz))

print(ikiyleCarpilmisListe)"""
#Çıktı [20, 40, 60, 80, 100]

#ikinci map örneği
def stringKontrol(s):
    return "eren" in s

isimListe = ["eren", "ahmet", "kemal", "mehmet eren", "mehmet ali", "dursun"]

#sonuc = list(map(stringKontrol, isimListe))
#print(sonuc)
#Çıktı [True, False, False, True, False, False]




#filter
sonuc1 = list(filter(stringKontrol, isimListe))
print(sonuc1)
#Çıktı ['eren', 'mehmet eren']




#lambda
carpma = lambda num : num * 3
print(carpma(3))
#çıktı 9

#lambda örnek
sonuc2 = list(filter(lambda s : "a" in s, isimListe))
print(sonuc2)
#çıktı ['ahmet', 'kemal', 'mehmet ali']