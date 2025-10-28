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