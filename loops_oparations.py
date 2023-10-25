# for  i in range(10):
#     print(i)

# greeting = 'Hello'

# for index,item in enumerate(greeting):
#     print(f"index: {index} letter: {item}")
    
    
    
    
    
    
#zip

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1,list2)))
for i in zip(list1,list2):
    print(i)