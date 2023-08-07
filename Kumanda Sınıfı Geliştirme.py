#kumanda sınıfı geliştirme

import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        
    def tv_aç(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor..")
            self.tv_durum="Açık"
            
    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapanıyor..")
            self.tv_durum="Kapalı"
            
    def ses_ayarları(self):
        while(True):
            cevap=input("\n\nSesi azalt: '<' \nSesi artır: '>' \nÇıkış: çıkış \n Bir seçim yapınız: " )
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses: ",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print("Ses: ",self.tv_ses)
            elif(cevap=="çıkış"):
                print("Ses güncellendi: ",self.tv_ses)
                break
            else:
                print("Yanlış bir seçim yaptınız lütfen doğru seçim yapınız!!")
                
    def kanal_ekle(self,kanal_ismi):
        print("\nKanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")
        
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal: ",self.kanal)
        
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumanda=Kumanda()

print("""
      TELEVİZYON UYGULAMASI
      
      1- TV Aç
      2- TV Kapa
      3- Ses Ayarları
      4- Kanal Ekle
      5- Kanal Sayısını Öğrenme
      6- Rastgele Kanala Geçme
      7- Televizyon Bilgileri
      
      Çıkmak için q'ya basın!!
      """)

while True:
    işlem=input("\n\nİşlem seçiniz: ")
    
    if(işlem=="q"):
        print("Program sonlandırılıyor..")
        print("Program sonlamdırıldı.")
        break
    elif(işlem=="1"):
        kumanda.tv_aç()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        kanal_isimleri=input("Kanal isimlerini virgül ile ayırarak girin: ")
        kanal_listesi=kanal_isimleri.split(",") # girilen değere göre ayırma işlemi tapıp listeye ekler..
        for eklenecekler in kanal_listesi:
           kumanda.kanal_ekle(eklenecekler)
    elif(işlem=="5"):
        print("Kanal sayısı: ",len(kumanda))
    elif(işlem=="6"):
        kumanda.rastgele_kanal()
    elif(işlem=="7"):
        print(kumanda)
    else:
        print("Geçersiz işlem..!")