a = 5
b = 3
b = a
print(a+b)

c = "hello"
print(c)

a = 5
b = 3
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b) # ondalıksız bölme
print("a % b = ", a % b)   # mod alma
print("a ** b = ", a ** b) # üs alma

#tip dönüşümleri
print(str(21) + str(21))
print(21+21)

int(9.45) # 9 float to int
float(9)  # 9.0 int to float

# kullanıcıdan veri alma
isim = input("ismi:")
print("merhaba", isim)

print("F","I","L","E", sep="_")

notA = input("1.Notgiriniz:")
notB = input("2.Notgiriniz:")
ortalama = (float(notA)+float(notB))/2
print("Ortalamanız:", ortalama)


if(notA>notB):
    print("1.Notunuz daha büyük")
else:
    print("2.Notunuz daha büyük")


listem = ["elma", "armut", "muz"]
print("elma" in listem)

if "muz" in listem:
    print("sepette muz var")
else:
    print("sepette muz yok")


range(10) # 0 dan 9 a kadar sayı üretir
range(10,29) # 10 dan 28 e kadar sayı üretir

for i in range(50,0 ,-4): # 50 den 0 a kadar 4 er 4 er azalarak gider
    print(i)

for i in range(0,33):
    if(i%2==0):
        print(i)

d=1
while(d!=0):
    d = int(input("sayı gir: "))
    print("girdiğin sayının karesi:", d*d)
    print("çıkmak için 0 gir")
print("döngü bitti")







