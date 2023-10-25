list1 = ["bmw","mercedes","opel","mazda"]

#kac elemani vardir? 
print(len(list1))

#listenin ilk ve son elemani
print(list1[0],list1[3])

#mazda elemanini toyata ile degistirin
list1[3] = "toyota"
print(list1[3])

#mercedes listenin bir elemanimidir
if "mercedes" in list1:
    print("true")
 ###### ayni islemin kolay yolu   
result = "mercedes" in list1    
print(result)


#listenin -2. index'indeki deger nedir?
print(list1[-2])

# listenin ilk 3 elemanini alin
print(list1[0:3])



# listenin son 2 elemanini "toyota ile renault ile degisir"
list1[-2:] = ["toyota","renault"]

#listenin uzerine 2 tane daha eleman ekleyiniz 
list1 = list1 + ["audi","tesla"]


#listenin son elemanini silin
del list1[-1]

#liste elemanlarini tersten yazdirin 
print(list1[::-1])

print(list1)




 ### farkli metotlar ====----- - -
 
numbers = [3,4] 
numbers.append(5)
print(numbers)

   