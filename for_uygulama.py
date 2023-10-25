sayilar = [1,3,5,7,12,19,21]

## sayilar listesindeki hangi sayilar 3'un katidir?

# for i in sayilar:
#     if i%2 == 1:
#         print(f"{i} sayisi tektir")
#     else:
#         print(f'{i} sayisi cifttir')

##  sayilar listesindeki sayilarin toplami nedir?

# sum = 0
# for i in sayilar:
#     sum = sum + i
# print(sum)


##  sayilar listesindeki tek sayilarin karesini aliniz.

# for i in sayilar:
#     if i%2 == 1:
#         print(i**2)


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

##   sehirlerden hangileri en fazla 5 karakterlidir.

# for i in sehirler:
#     if len(i)<=5:
#         print(f"{i} sehri en fazla 5 karakterdir.")
        
urunler =[
    {'model':'Samsung S6' , 'price':'3000'},
    {'model':'Samsung S7' , 'price':'4000'},
    {'model':'Samsung S8' , 'price':'5000'},
    {'model':'Samsung S9' , 'price':'6000'},
    {'model':'Samsung S10', 'price':'7000'}
]

## urunlerin toplam fiyati nedir ?

# sum  = 0
# for urun in urunler:
#     sum = sum + int(urun['price'])
# print(sum)

## urunlerin fiyati en fazla 500 olan urunleri gosteriniz.

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['model'])
        
    
    
    
    
    
    
    
    
    
    
    
    