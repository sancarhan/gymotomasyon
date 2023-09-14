import time
class Sirket:
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
    
    def yazilim(self):
        secim = self.secenekler()

        if secim == 1:
            self.yeniUye()
        if secim ==2:
            self.uyeCikar()
        if secim == 3:
            self.gelir()
        if secim == 4:
            self.gider()
        if secim == 5:
            self.kar()
        if secim == 6:
            self.cikis()

    def secenekler(self):
        secim = int(input(f"""\n***** {self.ad} 'e Hoşgeldiniz*****
        
        --Program Seçenekleri--
    1- Yeni Üyelik
    2- Üyelikten Çıkar
    3- Gelir
    4- Gider
    5- Kar
    6- Çıkış
        
Lütfen yapmak istediğiniz işlem kodunu giriniz (1-6) ="""))
        while secim < 1 or secim > 6:
            secim = int(input('Lüfen 1-6 arasında bir seçim yapınız ='))

        return secim

    def yeniUye(self):
        tamİsim = input('Üye ad-soyad giriniz =')
        meslek = input('Üye mesleğini giriniz =')
        ucret = input('Aylık üyelik ücretini giriniz =')
        cinsiyet = input('Üye cinsiyetini giriniz =')
        dYili = input('Üye doğum tarihini giriniz =')
        boy = input('Üye boyunu giriniz (cm) =')
        kilo = input('Üye kilosunu giriniz (kg) =')

        with open('uyelikler.txt','r',encoding='utf-8') as dosya:
            uyeListesi = dosya.readlines()
        
        if len(uyeListesi) == 0:
            sira = 1 
        else:
            sira = int(uyeListesi[-1].split(')')[0])+1

        with open('uyelikler.txt','a+',encoding='utf-8') as dosya:
            dosya.write('{}) {}-{}-{}-{}-{}cm-{}kg-{}TL\n'.format(sira,tamİsim,meslek,cinsiyet,dYili,boy,kilo,ucret))

    def uyeCikar(self):
        with open('uyelikler.txt','r',encoding='utf-8') as dosya:
            uyeler = dosya.readlines()
        xUyeler =[]
        print('Üye Listesi Yükleniyor...')
        for uye in uyeler:
            xUyeler.append(' '.join(uye[::].split('-')))
        for i in xUyeler:
            print(i)
            time.sleep(1)
        secim = int(input('Lütfen üyelikten çıkarılacak üyenin numarasını giriniz (1-{}) ='.format(len(xUyeler))))

        while secim < 1 or secim > len(xUyeler):
            secim = int(input('Lütfen (1-{}) arasnda bir değer giriniz ='.format(len(xUyeler))))
        uyeler.pop(secim-1)
        sayac = 1
        yUyeler = []

        for uye in uyeler:
            yUyeler.append(str(sayac)+')'+uye.split(')')[1])
            sayac += 1
        
        with open ('uyelikler.txt','w',encoding='utf-8') as dosya:
            dosya.writelines(yUyeler)

      
    def gelir(self):
        with open('uyelikler.txt','r',encoding='utf-8') as dosya:
            uyeler=dosya.readlines()

            toplamGelir = 0

            for ucret in uyeler:
                toplamGelir = toplamGelir + int(ucret.split('-')[-1][:-3])
            
            print('\n Ortalama Aylık Geliriniz =', toplamGelir,'TL')

    def gider(self):
        while True:
            print('''Masraf İşlemleri:
            1-Yeni Gider Ekle
            2-Çıkış''')
            secim= int(input('Yeni gider eklemek için 1e, çıkış için 2ye basınız ='))
            if secim == 1:
                giderTuru = input('Gider türünü yazınız =')
                giderTutar = int(input('Gider tutarını giriniz ='))
                with open('gider.txt','a+',encoding='utf-8') as dosya:
                    dosya.write(f'{giderTuru} - {giderTutar}TL\n')
            elif secim == 2:
                print('Anamenüye dönülüyor...')
                break
            else:
                secim= int(input('Yanlış seçim yaptınız!!!\nYeni gider eklemek için 1e, çıkış için 2ye basınız ='))

    def kar(self):
        with open('gider.txt','r',encoding='utf-8') as dosya:
            giderler = dosya.readlines()
            toplamGider = 0
            for masraf in giderler:
                toplamGider = toplamGider + int(masraf.split('-')[-1][1:-3])

        gider=toplamGider

        with open('uyelikler.txt','r',encoding='utf-8') as dosya:
            uyeler=dosya.readlines()
            toplamGelir = 0
            for ucret in uyeler:
                toplamGelir = toplamGelir + int(ucret.split('-')[-1][:-3])
        
        gelir=toplamGelir

        print('Hesaplanıyor...')
        time.sleep(1)
        print('Geliriniz =',gelir,'TL')
        time.sleep(1)
        print('Masraflar =',gider,'TL')
        time.sleep(1)
        print('Kar Miktarı =',(gelir-gider),'TL')
        time.sleep(3)
        

    def cikis(self):
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('BYE')
        sirket.calisma = False





sirket = Sirket('eSb Code Gym')

while sirket.calisma:
    sirket.yazilim()