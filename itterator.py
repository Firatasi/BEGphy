myList = [1,5,9,12,34]
iterator = iter(myList)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 5
print(next(iterator))  # Output: 9
print(next(iterator))  # Output: 12
print(next(iterator))  # Output: 34


iller = ["İzmir", "Ankara", "İstanbul", "Bursa", "Antalya", "Adana"]
iterator = iter(iller)

for sehir in iterator:
    print(sehir)
    if sehir == "İstanbul": #istanbul'da durdurmak için koşul yazdık
        break
    

class UsAl:
    def __init__(self,max):
        self.max = max
        
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

    usAl = UsAl(5)
    iterator = iter(usAl)
    for UsAl in iterator:
        print(UsAl)


class Fibonacci:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

fibo = Fibonacci(200)
for i in fibo:
    print(i, end="-")


#class olarak iterattor içeren girilen sayıya kadar olan çift sayıları yazdırma
class CiftSayilar:
    def __init__(self, max):
        self.max = max
        self.sayi = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.max:
            sonuc = self.sayi
            self.sayi += 2
            return sonuc
        else:
            raise StopIteration
ciftSayi = CiftSayilar(12)
for sayi in ciftSayi:
    print(sayi)

#uygulama2 dizinin elemanlarını topla ortalamasını bul
nums = [12,8,5,10,15]
class Ortalama:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
        self.total = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            self.total += self.numbers[self.index]
            self.index += 1
            return self.total / self.index
        else:
            raise StopIteration

#toplamı ve ortalama yazsırma yazdırma
toplam = 0
for num in nums:
    toplam += num
ortalama = toplam / len(nums)
print("Toplam:", toplam)   
print("Ortalama:", ortalama)     



#uyg3
import io

metin = """Python, Guido van Rossum tarafından 1991 yılında geliştirilen yüksek seviyeli bir programlama dilidir.
Python, okunabilirliği ve basit sözdizimi ile bilinir.  
Ayşe

Mehmet
Zeynep

"""
f = io.StringIO(metin)

satir_it = iter(f.readline, '') #boş satıra kadar oku (pass the callable, not its result)
bos_olmayan = 0
satir_no = 0
for line in satir_it:
    satir_no += 1
    if line.strip(): #boş olmayan satırları say
        bos_olmayan += 1
        print(f"Satır {satir_no}: {line.strip()}")
print(f"Toplam boş olmayan satır sayısı: {bos_olmayan}")
print(f"Toplam satır sayısı: {satir_no}")


#üçerli gruplara ayırma
ögrenciler = ["Ali", "Veli", "Ayşe", "Fatma", "Mehmet", "Zeynep", "Ahmet", "Can", "Deniz"]
it = iter(ögrenciler)
while True:
    grup = list()
    try:
        for _ in range(3):
            grup.append(next(it))
        print("Grup:", grup)
    except StopIteration:
        if grup:
            print("Kalan Öğrenciler:", grup)
        break


