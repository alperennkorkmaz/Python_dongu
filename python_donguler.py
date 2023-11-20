for i in range(1,101):
    print(i)


for i in range(1,101):
    if i%2==0:
        print(i)


for i in range(1,101):
    if i%2!=0:
        print(i)


for i in range(1,101):
    if i%3==0 or i%5==0:
        print(i)


sayi=input("sayı giriniz ")
for i in range(1,int(sayi)+1):
    print(i)


a = 1
while a < 11:
    a += 1
    print("bilgisayar yine çıldırdı!")


sayilar="123456789"
for sayı in sayilar:
    print(int(sayı)*2)


def dairealan(yaricap):
    alan=float(yaricap)*float(yaricap)*3.14
    print(alan)
    return alan
r=input("yarı çap giriniz ")
dairealan(r)


def dikalan (ukenar,kkenar):
    alan=float(ukenar)*float(kkenar)
    print(alan)
    return alan 
kk=input("kısa kenarı giriniz ")
uk=input("uzun kenarı giriniz ")
dikalan(kk,uk) 


def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('Merhaba\n', 10)


def emeklilik(isim, yaş):
    sonuç = 65 - int(yaş)
    if sonuç > 0:
        print(isim, "emekli oldunuz ")
    else:
        print(isim, "emekli olamadınız ")


ad = input("isim giriniz ")
sene = input("yaşınızı giriniz ")
emeklilik(ad, sene)


def emeklilik(isim, yaş):
    sonuç = 65 - int(yaş)
    if sonuç < 0:
        print(isim, "emekli oldunuz ")
    else:
        print(isim, "emekli olamadınız ")
while True:
    ad = input("isim giriniz çıkmak için q basınız ")
    if ad == 'q':
        break 
    sene = input("yaşınızı giriniz ")
    emeklilik(ad, sene)



liste1=["ali","mehmet","recep","ebu ubeyde"]
liste2=["emre","başkan","dihye","enes"]
while True:
        isim=input("isim giriniz çıkmak için q bas ")
        if isim =="q":
                break
        if isim in liste1:
                print("yukarı kata")
        elif isim in liste2:
                print("aşağı kata")
        elif isim not in liste1 and isim not in liste2:
                print("Listede adınız yoktur...")