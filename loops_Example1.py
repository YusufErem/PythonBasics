## Kullanicidan alinan sayinin asal sayi olup olmadigini kontrol ediniz,

while True:
    sayi = int(input("Lutfen Sayi giriniz "))
    if sayi<=1:
        print("sayi negatif veya sifir olamaz veya 1 olamaz.") and True
    else:break   
        

for i in range(2,sayi):
    if sayi%i == 0:
        print(f"{sayi} Asal Sayi degildir.")
        break
    else:
        print(f"{sayi} Asal Sayidir.")
         