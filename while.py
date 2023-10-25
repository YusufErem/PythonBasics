## 1-100 e kadar 

# x=0
# while x < 100:
#     print(x)
#     x = x + 1
# print('bitiii....!!!')
#---------------------------------------


##
# name = ''
# while not name.strip():
#     name = input("Isminizi giriniz . : ")
# print(f'Hosgeldin, {name} ')
#---------------------------------------
    

sayilar =[1,2,3,4,5,6,7,8,9]
    
## Sayilar listesini while ile ekrana yazdirin.

# i = 0
# while i<len(sayilar):
#     print(sayilar[i])
#     i = i + 1
#---------------------------------------
        
##  Baslangic ve bitis degerlerini kullanicaidan alip arasindaki
##  tum tek sayilari ekrana yazdirin 

# while True:
#     sayi1 = int(input("Lutfen baslangic sayisini giriniz"))
#     sayi2 = int(input("Lutfen bitis Sayisini giriniz"))
#     if sayi1>sayi2:
#         False
#     else:
        
#         while sayi1 < sayi2:
#             if(sayi1%2==1):
#                 print(sayi1)
#             else:
#                 True
#             sayi1 = sayi1 + 1
#         break
#---------------------------------------

##1 ile 100 arasindaki sayilari azalan sekilde yazin.

# i = 100
# while i >= 1:
#     print(i)
#     i-=1

#---------------------------------------
        
## Kullanicidan aldiginiz 5 sayiyi ekrana sirali sekilde yazdirin.
 
# numbers =[]

# while len(numbers)<5:
#     numbers.append(int(input("Lutfen sayi giriniz.")))
#     print(len(numbers))
# print(numbers)
   
      
 
## Kullanicidan aldiginiz sinirsiz urun bilgisini urunler listesinde sakla
## Urun sayisini kullaniciya sorun..
## Dictionary listesi yapisi olsun
## Urun Ekleme islemi bittikten sonra while ile fiyatina gore siralayin

urun_sayisi =int(input("Lutfen urun sayinizi giriniz:"))
urunler ={}
i= 0
while i < urun_sayisi:
    urun = input("Lutfen urun adinia giriniz: ")
    fiyat = int(input("Lutfen urunun fiyatini giriniz: "))
    urunler[urun] = fiyat
    i+=1

