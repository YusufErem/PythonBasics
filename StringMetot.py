#karakterin basindaki ve sonundaki karakterleri silmek icin kullanilar metot
result = " Hello World ".strip()
result = " Hello World".lstrip()
result = "Hello World ".rstrip()#hangi karakterleri silmek istersek bunun icine yazmamiz yeterli karaterleri

result = "Hello World ".upper()# Butun harfleri butur
result = "Hello World ".lower()# Butun karaktelri kucultur
result = "Hello World ".title()#Bas harfi buyutur.

result = "Hello World ".count('a')#a harfinin kac tane olugunu yazar
result = "Hello World ".count("ll",0,10)#0 inci index ile 10'uncu index arasinda kac tane var onu yazar,

result = "Hello World ".startswith("www")#Hello world "www ile mi basliyor"
result = "Hello World ".endswith(".com")# Hello wordl ".com" ile mi bitiyor.

result = "Hello World ".find("Hello")#hello ifadedsi hello world icinde var mi ona bakar ilk indexi bize verir
result = "Hello World ".find("Hello",0,10)#0 ile 10'uncu index arasinda ara
#result = "Hello World :".index("hello")#Hello'nuin basindaki index numarasini verir.

result = "Hello World ".isalpha()#alfabetik mi oludugnu sorgular.
result = "Hello World ".isdigit()#rakam olup olmadigini sorgular.

result = "Hello World ".center(10,"*")#topam 10 karakter icine sigdirir basina sonuna da yildiz ekler dolduramadigi yere


result = "Hello World ".replace(" ","-")#Bosluk karakterleri yerine "-" ekler.


result = "Hello World ".split(" ")#bosluk gordugu yerde ayirip aayri bir dize elemani yapar






print(result)



