names = ['ALi','Yagmur','Hakan','Deniz']
years = [1998,2000,1998,1987]


#1-) Cenk ismini listenin sonuna ekleyin
names.append('Cenk')

#2-) Sena Ismini listenin basina ekleyiniz. 
names.insert(0,"Sena")

#3-) Deniz ismini listeden Siliniz. 
#print(names)
names.pop()

#4-) Deniz isminin indexi nedir? 
names.index("Deniz")

#5-) Ali Listenin bir elemani midir? 
print(names.count("ali"))

#6-) Listenin Elemanlari terse cevirin
names.reverse()

#7-) Liste elemanlarini Alfabetik olarak sirayiniz.
names.sort()

#8-)Years listesinin elemanlarini rakamsal olarak buyukluge siralayiniz.
years.sort()

#9-) str ="chevrolet, dacia" dizisini listeye ceviriniz.

str = ["Chevrolet","Dacia"]

#10-) years dizisinin een buyuk ve en kucuk elemani nedir? 

years.sort()

#11-) years listesininde kac tane 1998 elamani vardir? 
years.count(1998)

#12-) years elamanlarinin tamanini siliniz. 
years.pop()

#13-) Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz,\
brand = []
brand[0] = str(input("lutfen markanizi giriniz"))
brand[1] = str(input("lutfen markanizi giriniz"))
brand[2] = str(input("lutfen markanizi giriniz"))
print(brand[::])





