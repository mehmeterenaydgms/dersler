#Sonsuz bir dögüye alıyoruz
while True:
    #koda herhangi bir etkisi olmuyor kodu çalıştırıyor ama diğer kullanacağımız şeyler için lazım.
    try:
        #Kullanıcıdan girdi alıyoruz.
        yeniIntDegisken = int(input("Bir numara giriniz :"))
        
        
    #eğer yanlış bir durum olursa örneğin kullanıcının verdiği girdi int değil de string bir değer olursa uygulanacak kısımı yazıyoruz
    except:
        print("Üzgünüm, sanırsam yazdığın şey bir numara değil")
        continue
        #tekrar while döngüsüne aldım ki böylece kullanıcı yeniden doğru değeri girsin
    
    
    #eğer girdiği şey doğru ise ve bir sıkıntı çıkmaz ise olucak işlemi yaptırıyorum
    else:
        print("Teşekkürler numara alındı")
        break
        #kullanıcı doğru işlemi yaptığı için while döngüsünü bitiriyorum
    
    
      