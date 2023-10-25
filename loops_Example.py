'''
    1-100 arasinda rastgele uretilecek bir sayiyi assagi yukari ifadelerle
    buldurmaya calisin
    ##Random modulu icin python random seklinde arama yapin
    100 uzerinden puyanlama yapin
    her soru 20 puan
    Hak bilgisi kullanicindan alin ve her sou belirten can sayisi
    uzerinden hesaplansin.

'''
from random import random
from random import randint

number = randint(1,100)
print(number)

kacHak = int(input("Kac tane deneme yapmak istiyorsunuz ?"))

x= 0
while x<kacHak:
    tahmin = int(input("Lutfen bir sayi tahmin edin? "))
    if tahmin == number :
        print(f"Tebrikler Dogru tahmin yaptiniz yaptiniz. Puaniniz{100/(x+1)}")
        break
    elif kacHak == x+1:
        print("Mallesef Bilemediniz Puaniniz 0")
    elif tahmin>number:
        print("Sayinizi Azaltin.")
    elif tahmin<number:
        print("Sayinizi Arttirin.")    
    
    x = x +1
    
    