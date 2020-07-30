# -*- coding: utf-8 -*-

print("Merhaba ideal kilo hesaplmaya hoş geldiniz")

cinsiyet=input("Lütfen cinsiyet belirtiniz: E/K ")
giris=cinsiyet.upper()

boy=int(input("Lütfen boyonuzu cm olarak giriniz: "))

kilo=int(input("Lütfen Kilonuzu kg olarak giriniz: "))

ideal_kilo=0
sonuc=0
try:
    if (giris=="E"):
        ideal_kilo=50+2.5*((boy/2.54)-60)
        if(kilo>ideal_kilo):
            sonuc=kilo-ideal_kilo
            print(f"Kilonuz ideal kilonuzdan {round(sonuc,1)} kg fazla :( ")
            
            print("İdeal kilonuz:" ,round(ideal_kilo,1),"kg olmalı." )
        else:
       
            sonuc=ideal_kilo-sonuc
            print(f"Kilonuz ideal kilonuzdan {round(sonuc,1)} kg düşük ")
            
            print("İdeal kilonuz:" ,round(ideal_kilo,1),"kg olmalı." )
    
    else:
       ideal_kilo=45.2+2.3*((boy/2.54)-60)
       if(kilo>ideal_kilo):
            
            sonuc=kilo-ideal_kilo
            print(f"Kilonuz ideal kilonuzdan {round(sonuc,1)} kg fazla :( ")
            
            print("İdeal kilonuz:" ,round(ideal_kilo,1),"kg olmalı." )
       else:
            sonuc=ideal_kilo-sonuc
            print(f"Kilonuz ideal kilonuzdan {round(sonuc,1)} kg düşük ")
            
            print("İdeal kilonuz:" ,round(ideal_kilo,1),"kg olmalı." )
        
        
except:
     print("hatalı giriş lütfen değerleri kontrol edip tekrar deneyin")
