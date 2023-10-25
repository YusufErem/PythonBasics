numbers = [x for x in range(10)]
print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList=[letter for letter in myString]
print(myList)

years = [1999,1998,1994,1995]
ages = [2023-year for year in years]
print(ages)

results = [x if x%2==0 else"Tek" for x in range(1,10)]
print(results)


result = []
for x in range(3):
    for y in range(3):
        result.append(x,y)
        
        
print(result)