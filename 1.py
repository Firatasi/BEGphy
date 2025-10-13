#Variables in Python
x = 5
y = "John"
print(x)
print(y)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))
print(type("Hello, World!"))

#Single or Double Quotes?
x = "John"
# is the same as
x = 'John'


#Case-Sensitive
a = 4
A = "Sally"

print(a)
print(A)

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

###
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)


#The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)


#### Global Variables
#use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)


######## Python Data Types ######
#Built-in Data Types
x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x)) #complex number

#Sıralı (ordered) koleksiyon. Elemanların eklenme sırası korunur. Tekrarlayan (duplicate) elemanlara izin verir.
x = ["apple", "banana", "cherry"]
print(type(x))

#tuple
x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

#Set: Sırasız (unordered), benzersiz (unique) elemanlardan oluşan koleksiyon. Tekrar eden elemanlara izin vermez
x = {"apple", "banana", "cherry"}
print(type(x))
x = {"apple", "banana", "cherry","apple"}
print(x)

## list, set, tuple farkı
# List
mylist = [1, 2, 2, 3]
mylist[0] = 100
print(mylist)  # [100, 2, 2, 3]

# Tuple
mytuple = (1, 2, 2, 3)
#mytuple[0] = 100  #  Hata! tuple değiştirilemez

# Set
myset = {1, 2, 2, 3}
print(myset)   # {1, 2, 3}  (tekrar otomatik silindi)
#set de indeks yoktur, doğrudan değiştiremezsin. Ancak .add() ve .remove() ile eleman ekleyip çıkarabilirsin.

#list = sıralı ve değiştirilebilir

#tuple = sıralı ama değiştirilemez

#set = sırasız, benzersiz elemanlardan oluşur,Once a set is created, you cannot change its items, but you can add new items.


#String are Arrays
a = "Hello, World!"
print(a[1])

print(len(a))

for x in "banana":
  print(x,end=" ") #yan yana yazdırır end parametresi ile
  
#Check String
txt = "The best things in life are free!"
print("free" in txt)
print("expensive"  in txt)
print("moon" not in txt)

#Slicing
b = "Hello, World!"
print(b[2:5])

print(b[:5])

print(b[2:])

print(b[-5:-2])

#Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)


#String Methods
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

x = txt.endswith(".")
print(x)


txt = "CompanyX123"
x = txt.isalpha()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)

#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#######BURDAN DEVAMMMMMMM!!!!!!!!!!!!
#Operators
# Basit hesap makinesi
a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

# Aritmetik operatörler
print("Toplama:", a + b)      # +
print("Çıkarma:", a - b)      # -
print("Çarpma:", a * b)       # *
print("Bölme:", a / b)        # /
print("Mod (kalan):", a % b)  # %
print("Üs alma:", a ** b)     # **

# Karşılaştırma operatörleri
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

# Mantıksal operatörler
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > b):", not(a > b))


#Python Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)

print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist[1] = "blackcurrant"
print(thislist)

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#loop using list comprehension
thislist = ["apple", "banana", "cherry"]
[x for x in thislist]



#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist) 

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#remove item from list
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#count item in list
fruits = ['apple', 'banana', 'cherry','apple']
x = fruits.count("apple")
print(x)


#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

thisdict["year"] = 2018
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


for x in thisdict:
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

##### Python If ... Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


### while loop
i = 1
while i < 6:
  print(i)
  i += 1


#with break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Functions
def my_function():
  print("Hello from a function")

my_function()


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


##bu kod hata verecek
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, 
# add a  * before the parameter name in the function definition.

def my_function(*args):
  print("The youngest child is " + args[2])

my_function("Emil", "Tobias", "Linus")
#my_function("Emil", "Tobias")# hata verir çünkü 3. eleman yok


def demo_func(*args):
    if len(args) >= 3:
        print("2. indeks (3. parametre):", args[2])
    elif len(args) >= 2:
        print("2. parametre:", args[1])
    else:
        print("Yeterli parametre yok")

# Kullanım
demo_func(10, 20, 30)   # 3 parametre → args[2] = 30
demo_func(10, 20)       # 2 parametre → args[1] = 20



#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name
def my_function(**kwargs):
  print("His last name is " + kwargs["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
my_function(fname = "Tobias", lname = "Refsnes",middle="None")



#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

######File Handling
#Open a File
f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "r")
print(f.read(5))
f.close() 

f = open("demofile.txt", "r")
print(f.readline())


f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close() 

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close() 

import os
os.remove("demofile.txt")

#Check if File exist:
if os.path.exists("demofile.txt"):
  print("The file exists.")
else:
  print("The file does not exist.")

#delete folder
#delete an entire folder, use
import os
os.rmdir("myfolder")
  
