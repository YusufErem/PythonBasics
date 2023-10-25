#value typle -- >>>  int gibi string gibi

x =10
y =20
x = y 
y = 23
print(x,y)

# referance tyole -->>> List gibi 

a =  ["ahmet","mehmet"]
b =  ["ahmet","mehmet"]
a=b
b[0] = "grape" # Burada yaptigim degisilik yukariyida etkiledi
                #cunku burada yaptigimiz atama islemi adress kismini atar
                #deger kismini atamaz sonuc olarak ayni degere giderler 
print(a,b)

