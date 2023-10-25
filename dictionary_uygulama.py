#Bilgileri verilen ogrencileri kullanicidan aldgininz bilgilere gore dictionary icinde saklayiniz

#Ogrenci numarasinin kullanicidan alip ilgili ogrencinin bilgilerini gosteriniz


ogrenciler= {}

number = input("Lufen Ogrenci numaranizi giriniz: ")
name = input("Lutfen adinizi giriniz: ")
surname = input("Lutfen soy adinizi giriniz: ")
phone = input("Lutfen telefon numaranizi giriniz: ")

ogrenciler[number] = {"ad":name,"soyad":surname,"telno":phone}



numara = input("lutfen okul numaranizi giriniz : ")
print(ogrenciler[numara])



