 #q-1) 3 notunun ortlalamasini hesaplayan
 ###   ve bu sonucun  araliklara gore  derecesini belirtiniz.
 
# birincisinav = int(input("Birinci sinav sonucunuzu giriniz: "))
# ikincisinav = int(input("Ikinci sinav sonucunuzu giriniz: "))
# ucuncusinav = int(input("Ucuncu sinav sonucunuzu giriniz: "))

# toplam = birincisinav + ikincisinav + ucuncusinav
# ortalama = toplam/3
# if ortalama < 0 and ortalama >100:
#     print("yanlis bilgi girdiniz")
# elif 0 < ortalama <= 24 :
#     print("notunuz 0")
# elif 24 < ortalama <= 44 :
#     print("notunuz 1")
# elif 44 < ortalama < 70 :
#     print("notunuz 2")
# else:
#     print("notunuz 3")
      

#q-2) Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesaplayiniz.

#1. bakim -- 1.yil
#2. bakim -- 2.yil
#3. bakim -- 3.yil
# sure hesabini alinan gun ay yil bilgisine gun basli hesaplayiniz
#   datetime modulunu kullanmaniz gerekir..
import datetime
from datetime import timedelta
from datetime import date


yil = int(input("Aracinizin trafige cikis yil'ini yaziniz: "))
ay = int(input("Aracinizin trafige cikis ay'ini yaziniz: "))
gun = int(input("Aracinizin trafige cikis gun'unu yazini: "))

d = date(yil,ay,gun)

gecenSure =date.today() -d

print(gecenSure)
