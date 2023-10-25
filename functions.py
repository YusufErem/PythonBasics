
# def sayHello():
#     name = input("Adinizi Giriniz.")
#     print(f"Hello {name}")

# sayHello()

# def helloWorld(name):
#     return name
# name = helloWorld("Yusuf")
# print(name)
     
     
def total(num1,num2):
    return num1+num2    
     
result = total(1,2)

def ageCalculatror(bd):
    return 2023-bd

#result = ageCalculatror(1999)


##################################

#hatirlatma listleri birbirine esitlerken kaynaklari esitlersen sonuclari da degisir

sehirler = ["Istanbul","Ankara"]
# n = sehirler ## Bu sekilde yapmamiz n uzerinde degisiklik yaparsak digeri de etkilenir anlamina gelir

n = sehirler[:]# Bu sekilde yapmamiz kopyasini cikardigimiz anlamina gelir
n[0] = "Ankara"
# print(sehirler)######  HATIRLATMAAA!!
# print(n)

####################################

def add(*params):
    return sum(params)

#print(add(10,20,0))


def displayUser(**args):
    for key,value in args.items():
        print(f"{key} is {value}")

#displayUser(name = "Cinar", age = 2, city = "Istanbul")    


def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

#myFunc(10,20,40,50,50, name = "ali")

#################################################
#                   UYGULAMA                     #

#gonderilern bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yaziniz

# kelime = input("Lutfen girmek istediginiz kelimeyi giriniz")
# sayi = int(input("Lutfen kac defa tekrarlamak istediginizi giriniz"))

# def tekrarla(kelime,sayi):
#     i = 0 
#     while i<sayi:
#         print(kelime)
#         i = i + 1

# tekrarla(kelime,sayi)
        
 
 
 ## kendine gelen sinirsiz sayida parametreyi bir listeye ceviren fonksiyon yazin
 
 
def listConverter(*args):
    for liste in args:
        liste = args
        return liste
     
print(listConverter(10,20,40,50,50))




## Gonderilen 2 sayi arasindaki tum asal sayilari bulan bir fonkisyon yaziniz

#asal sayi sadece kendine ve 1'e bolunen sayidir,


def asalSayibul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if (sayi%i==0):
                    break
            else:
                print(sayi)
sayi1 = int(input("Sayi1'i gir"))
sayi2 = int(input("Sayi2 yi giriniz."))


### Gonderilen bir sayinin tam bolenlerini bir liste seklinde dondurunuz



def tamBolenBul(sayiT):
    tamBolenListe =[]
    
    for tamBolenSayi in range(1,sayiT+1):
        if sayiT%tamBolenSayi==0:
            tamBolenListe.append(tamBolenSayi)
        else: continue
    print(tamBolenListe)
sayiVer = int(input("Lutfen tam bolenlerini bulmak istediginiz sayiyi giriniz."))

tamBolenBul(sayiVer)