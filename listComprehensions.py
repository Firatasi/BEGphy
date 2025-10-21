sayilar = [18, 22, 5, 3, 43, 25]
yeni_sayilar = [sayi * 2 for sayi in sayilar]
print(yeni_sayilar)

#uzun hali
dene = []
for sayi in sayilar:
    dene.append(sayi * 2)
print(dene)


plakalar = [1, 6, 34, 35, 41, 67]
yeni_plakalar = [plaka ** 10 for plaka in plakalar]
print(yeni_plakalar)


listem = [characters for char in ["Python", "Java", "C#", "JavaScript"] for characters in char]
print(listem)

#çift sayılar
cift_sayilar = [sayi for sayi in range(1, 101) if sayi % 2 == 0]
print(cift_sayilar)

numbers = [-1, -2, 0, 1, 2]
pozitif_sayilar = [num for num in numbers if num > 0]
print(pozitif_sayilar)

yy = ["çift sayi" if num % 2 == 0 else "tek sayi" for num in range(8)]
print(yy)

sicakliklar = [10, 20, 30, 40, 50]
farenheit = [((9/5) * derece + 32) for derece in sicakliklar]
print(farenheit)

words = ["hello", "world", "python", "is", "awesome"]
modified_words = [word if len(word)>3 else "kısa kelime" for word in words]
print(modified_words)

notlar = [55, 70, 85, 100, 90]
harf_notlari = ["A" if not_ >= 90 else "B" if not_ >= 80 else "C" if not_ >= 55 else "D" for not_ in notlar]
print(harf_notlari)

names = ["Ali", "Veli", "Ayşe", "Fatma","Firat"]
greetings = ["A" + name[1:] if name[0]=="A" else "B" + name[1:] for name in names]
print(greetings)

#list comprehensions with functions

def digitSum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

list1 = [123, 456, 789]
list2 = [digitSum(num) for num in list1 if num%2 != 0]
print(list2)

matris = [  [j for j in range(3)] for i in range(5)]
print(matris)

isim = "FIRAT"
listem = [chr for chr in isim] #her karakteri listeye atar  
print(listem)


#lambda functions with list comprehensions
x = lambda a: a * 2 #tek parametreli a yerine a*2 döner a yerine 5 geliyorsa 10 döner
print(x(5))

y = lambda a,b: a+b #iki parametreli a ve b toplanır
print(y(3,5))

z = lambda a,b,c: a*b*c #üç parametreli a,b,c çarpılır
print(z(2,3,4)) 

def math(n):
    return lambda a: a * n #n parametresi dışarıdan alınır a parametresi fonksiyon çağrılırken alınır
doubler = math(2) #n=2 olur
print(doubler(11)) #a=11 olur 2*11=22 döner

tripler = math(3) #n=3 olur
print(tripler(11)) #a=11 olur 3*11=33 döner

even_numbers = [2,4,6,8,10]
squared_numbers = [(lambda x: x**2) (i) for i in even_numbers] #her elemanı karesini alır
print(squared_numbers) 

words = ["hello", "world", "python","ha"]
word_length = [word + "kelimesi dırejdır" if len(word) > 3 else word + "kelimesi kındır" for word in words]
print(word_length)




numbers = [1,2,3,4,5,6,7,8,9]

def square(n):
    return n*n

result = list(map(square, numbers)) #map fonksiyonu ile her elemanı square fonksiyonuna gönderir
print(result)



words = ["hello", "world", "python","ha"]
büyük_harf = list(map(lambda word: word.upper(), words)) #her elemanı büyük harfe çevirir
print(büyük_harf)   


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]    
summed = list(map(lambda x,y: x+y, list1, list2)) #iki listeyi eleman eleman toplar
print(summed)

sayilar = list(map((lambda x: x%2),[i for i in range(2,44)])) #2 den 43 e kadar olan sayılardan çift olanları alır
print(sayilar)


isimler = ["Ali", "Veli", "Ayşe", "Fatma","Firat"]
bas_harf = list(map(lambda name: "B" + name[1:] if name[0]=="A" else "A" + name[1:], isimler)) #A ile başlayan isimlerin başına B, diğerlerinin başına A ekler
print(bas_harf)



list1 = [10,20,5,15]
list2 = [7,25,10,5]
cikar = [sonuc for sonuc in list(map(lambda x1,y1: x1-y1, list1, list2)) if sonuc > 0 ]
print(cikar)

#filter function with list comprehensions
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
vowels = list(filter(lambda x: x in 'aeiou', letters)) #sesli harfleri alır
print(vowels)   


seq = [0,1,2,3,4,5,8,13]
result = list(filter(lambda x: x%2 != 0, seq)) #tek sayıları alır
print(result)


def is_multiple_of_3(num):
    return num % 3 == 0 #3 ün katı olan sayıları alır

filtered_numbers = list(filter(lambda x: is_multiple_of_3(x), range(1, 121))) #1 den 20 ye kadar olan sayılardan 3 ün katı olanları alır
print(filtered_numbers)


#asal sayılar
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
primes = list(filter(is_prime, range(1, 101))) #1 den 100 e kadar olan asal sayıları alır
print(primes)

#************************************************************************5.hafta

numberes = [12,15,20,24,30,35,40,45,48,50,60,75]
#bir liste halinde verilen sayıların sadece sadece çift ve 3 ün katlarını al

filtered = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numberes))
kare_al = list(map(lambda x: x**2, filtered))
print(kare_al)



kisiler = ["Ali", "Veli", "Ayşe", "Fatma","Firat","Ahmet","Mehmet"]
tarihler = [1990, 1985, 2000, 1995, 1980, 1975, 1965]
kisiler_tarihler = list(zip(kisiler, tarihler)) #iki listeyi birleştirir
print(kisiler_tarihler)


filtrelenmis_kisiler = list(filter(lambda x: x[1] > 1990, kisiler_tarihler)) #1990 dan büyük olanları alır
print(filtrelenmis_kisiler)

dosyalar = ["document.txt", "image.png", "script.py", "archive.zip", "presentation.pptx"]
#uzantısı .py ve .txt olan dosyaları al
filtrelenmis_dosyalar = list(filter(lambda x: x.endswith('.py') or x.endswith('.txt'), dosyalar))
print(filtrelenmis_dosyalar)


employees = [
    {"name": "Alice","salary":90000, "age": 30, "department": "IT"},
    {"name": "Bob","salary":50000, "age": 24, "department": "Engineering"},
    {"name": "Charlie","salary":70000, "age": 29, "department": "Finans"},
    {"name": "David","salary":65000, "age": 35, "department": "Engineering"},
    {"name": "Eve","salary":120000, "age": 28, "department": "HR"}
]
#maaşı 60bin üstü olanları al lambda ve filtre kullan
high_earners = list(filter(lambda x: x['salary'] > 60000, employees))
print(high_earners)


#any kullanımı
myList = [False,True,False]
result = any(myList) #en az bir tane True varsa True döner
print(result)

#All kullanımı
myList2 = [True,True,True]
result2 = all(myList2) #tüm elemanlar True ise True döner
print(result2)

myList3 = [True,False,True]
result3 = all(myList3) #tüm elemanlar True değilse False döner
print(result3)

#listede en az bir pozitif sayı olup olmadığını kontrol et
numbers = [-1, -2, -3, 0]
has_positive = any(num > 0 for num in numbers)
print(has_positive)

#listede tüm sayılar pozitif mi kontrol et
all_positive = all(num > 0 for num in numbers)
print(all_positive)

#bir listede tüm kelimeler 3 karakterden uzun mu kontrol et
words = ["cat", "dog", "elephant"]
all_longer_than_3 = all(len(word) > 3 for word in words)
print(all_longer_than_3)

#bir listede en az bir kelime 5 karakterden uzun mu kontrol et
some_longer_than_5 = any(len(word) > 5 for word in words)
print(some_longer_than_5)

datam = {"ad": "Fırat",
         "yas": 25,
         "meslek": "Mühendis",
         "sehir": None}
is_empty = any(any(d==None for d in datam.values()))
print(is_empty)

#sorted fonksiyonu,bir sayı dizinini küçükten büyüğe sıralama
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)

#çalışanları maaşlarına göre küçükten büyüğe sıralayalım, sorted kullan
employees = [
    {"name": "Alice","salary":90000, "age": 30, "department": "IT"},
    {"name": "Bob","salary":50000, "age": 24, "department": "Engineering"},
    {"name": "Charlie","salary":70000, "age": 29, "department": "Finans"},
    {"name": "David","salary":65000, "age": 35, "department": "Engineering"},
    {"name": "Eve","salary":120000, "age": 28, "department": "HR"}
]

sorted_employees = sorted(employees, key=lambda x: x['salary']) #maaşa göre küçükten büyüğe sıralar
print(sorted_employees) 

#çalışanları yaşlarına göre büyükten küçüğe sıralayalım, sorted kullan
sorted_employees_by_age = sorted(employees, key=lambda x: x['age'], reverse=True) #yaşa göre büyükten küçüğe sıralar
print(sorted_employees_by_age)


numbers = [5, 2, 9, 1, 5, 6]
min_number = min(numbers) #en küçük sayıyı bulur
max_number = max(numbers) #en büyük sayıyı bulur
print("Min:", min_number, "Max:", max_number)

list1 = [10,20,5,15]
list2 = [7,25,10,5]
min_values = list(map(min,list1, list2)) #iki listeyi eleman eleman karşılaştırır ve en küçüğünü alır
print(min_values)

max_values = list(map(max,list1, list2)) #iki listeyi eleman eleman karşılaştır
print(max_values)

#sum ve raund
numbers = [1.5, 2.3, 3.7, 4.2]
total = sum(numbers) #toplamını alır
rounded_total = round(total, 2) #toplamı 2 ondalık basamağa yuvarlar
print("Total:", total, "Rounded Total:", rounded_total)
#bir liste içindeki sayıların toplamını ve ortalamasını bul
numbers = [10, 20, 30, 40, 50]
total = sum(numbers) #toplamını alır
average = total / len(numbers) #ortalamasını alır
rounded_average = round(average, 2) #ortalamasını 2 ondalık basamağa yuvarlar
print("Total:", total, "Average:", rounded_average)



#uygulama

list1 = [5,3,10,15]
list2 = [4,7,1,8]
#list1 ve list2'nin karşılık gelen öğelerini toplamak için map fonksiyonunu kullanın ve list comprehension özelliğini kullanarak,toplam değeri 10 eşik değerinden küçük olan sonuçları filtreleyin.Yani onları almayın,yalnızca 10'dan büyük olan toplamlaro içeren son listeyi döndürün.

summed_filtered = [result for result in map(lambda x,y: x+y, list1, list2) if result > 10]
print(summed_filtered)
print(list1)
print(list2)


names = ["alice", "bob", "charlie", "david", "eve"]
#her ismin ilk harfini büyük yapmak için map fonksiyonunu kullanın ve liste kavrama özelliğini kullanarak 3 karakterden az olan isimleri filtrekleyiniz yani  3 ten az olanları almayın, 3 harften daha uzun olan büyük harfli isimlerin son listesini dödndürü.
capitalized_filtered = [name.upper() for name in map(lambda x: x.capitalize(), names) if len(name) > 3]
print(capitalized_filtered)
print(names)

#listenin sadece çift sayılarını alıp,busayıları 2 ile çarparak ynei bir liste oluşturmanızdır.Ayrıca,yeni listenin her elemanı için şunu kontrol etmelisiniz: eğer sayı 10'dan büyükse,o sayının "büyük" olarak değiştirilmesini,değilse sayının olduğu gibi kalmasını sağlayın, bu işlemi list chomprehensions kullanarak yapın.
original_numbers = [4, 7, 9, 12, 5, 2, 15, 8]
modified_numbers = [num * 2 if num * 2 <= 10 else "büyük" for num in original_numbers if num % 2 == 0]
print(modified_numbers)

#recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(0)) # 0! = 1
print(factorial(1)) # 1! = 1
print(factorial(14)) # 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
print(fibonacci(10)) # İlk 10 Fibonacci sayısı
print(fibonacci(1))  # İlk 1 Fibonacci sayısı
print(fibonacci(2))  # İlk 0 Fibonacci sayısı


