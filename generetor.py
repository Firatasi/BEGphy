def simpleGeneretor():
    yield 1
    yield 2
    yield 3

for value in simpleGeneretor():
     print(value)


x = simpleGeneretor()
print(next(x))
print(next(x))

#fibonacci ***********************************************
def fibonacci(limit):
     a,b =0,1
     while a < limit:
        yield a
        a,b =b ,a+b

fibo = fibonacci(100)
for f in fibo:
    print(f, end="-")


list1 = [ i     for   i in range(0,50,2)]
print(list1)

list2 = ( i     for i in range(0,50,2)) #generator expression
print("list2: ",list2)
print(next(list2))
print(next(list2))


def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

path = "/Users/Firatt/Desktop/-/üDers/Python/Nutuk.txt"
line = next(read_file(path))
print(line)


#generetor iterotor nedir? bakalım


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

x = generate_prime_numbers()
print(next(x))
print(next(x))
print(next(x))

def log_filter_read(file_path, ip):
    with open(file_path, 'r') as file:
        for line in file:
            if ip in line:
                yield line

x = log_filter_read("/Users/Firatt/Desktop/-/üDers/Python/log.txt", "192.168.1.1")
for i in x:
    print(i)


def kare_al():
    sayi = 0
    while True:
        kare = sayi**2
        yield kare
        sayi += 1

y = kare_al()
print(next(y))
print(next(y))
print(next(y))

def dosya_adi_uret(on_ad, baslangic, bitis, uzanti):
    for i in range(baslangic, bitis):
        yield f"{on_ad}{i}.{uzanti}"

dosya_adi = dosya_adi_uret("resim_", 1, 9, "png")
for i in dosya_adi:
    print(i)
    