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