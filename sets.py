fruits = {"orange","apple","watermelon"}

# indexlenemez diziler gibi (SET)

for x in fruits:
    print(x)
fruits.add("cherry")#   ekler

print(fruits)
fruits.update(["merhaba","selam"])#bunlari ekler 
print(fruits)

fruits.remove("merhaba")#merhaba siler
fruits.discard("apple")#apple siler
fruits.pop() #rasgele bir elemani siler
fruits.clear#butun elemanlari siler




myList =[1,2,3,4,5,3,3,3,3]
print(myList)
print(set(myList))#Set edersek listede tekrar eden sayilar silinir.




