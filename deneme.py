
sayilar=[22,24,26,32,36]
yeni_sayilar=[  i*2    for i in sayilar]
print(yeni_sayilar)

#uzun hali
dene=[]
for i in sayilar:
    dene.append(i*2)

print(dene)

plaka_kodlari=[45,35,6,34,48,32]
yeni_plaka_kodlari=[i**2    for i in plaka_kodlari]
print(yeni_plaka_kodlari)

listem=[charecter   for charecter in [1,2,3]]
print(listem)


aa=[ i       for i in range(12) if i%2==0]
print(aa)


numbers=[-2,-7,-9,-4,8,21,54]
positive_numbers=[ i     for i in numbers if i>0]
print(positive_numbers)


numbers=[1,6,3,8,5,9]
modified_numbers= [i*3     for i in numbers if i>5]
print(modified_numbers)


yy=[  "çift sayı"  if i%2==0  else "tek sayı"  for i in range(8)]
print(yy)

sicaklik=[32,100,-40,212,0]
donusturulmus_sicaklik=[ ((i-32)*5/9) if i>0 else i  for i in sicaklik]
print(donusturulmus_sicaklik)


words=["apple","cat","banana","dog"]
modified_words=[ word   if len(word)>3  else "kısa kelime"  for word in words]
print(modified_words)

notlar=[85,92,58,77,99]
harf_karsiliklari=[ 'A'  if  nott>=90  else  'B' if nott>=80  else 'C' if nott>=70 else 'D'    for nott in notlar]
print(harf_karsiliklari)

names=['M.John','F.ALice','M.Bob','F.Diana']
greetings=[ 'Mr'+name[1:]  if name[0]=='M' else 'Ms'+name[1:]  for name in names]
print(greetings)


#list comprehesion with functions
def digitSum(n):
    dsum=0
    for ele in str(n):
        dsum+=int(ele)
    
    return dsum

list1=[367,111,562,945,6726,873]
new_list1=[ digitSum(i)   for i in list1 if i%2!=0]
print(new_list1)

matris=[  [ j for j in range(3)]  for i in range(5)]
print(matris)

isim="MAKÜ BSM"
listem=[ chr   for chr in isim]
print(listem)


#lambda Kullanımı

x=lambda a: a+10
print(x(5))

y=lambda a,b: a+b
print(y(3,4))

z=lambda a,b,c: a+b+c
print(z(7,8,9))


def math(n):
    return lambda a: a**n

kare=math(2)
print(kare(8))

kup=math(3)
print(kup(7))

even_numbers=[2,4,6,8,10,12]
squared_numbers=[ (lambda x:x**2) (i)  for i in even_numbers]
print(squared_numbers)


words=["apple","cat","banana","dog"]
word_length=[   (lambda x:x+" kelimesi uzundur" 
             if len(x)>3 else x+" kelimesi kısadır" ) (word)  for word in words]

print(word_length)


#Mpython'da Map Kullanımı
numbers=[1,3,5,9,10,4]

def square(num):
    return num**2

result=list(map(square,numbers))
print(result)


words=['python','map','function']
buyuk_harf= list(map(str.upper,words))
print(buyuk_harf)

list1=[1,2,3]
list2=[4,5,6]

toplam_liste= list(map((lambda x1,x2: x1+x2),list1,list2))
print(toplam_liste)


sayilar= list(map((lambda x: x%2),[ i  for i in range(2,44)]))
print(sayilar)


isimler=['Elif','Berk','Can','Ece','Emirhan']
bas_harf=[ isim[0] for isim in list(map(lambda x: x,isimler)) if len(isim)<4]
print(bas_harf)


list1=[10,20,5,15]
list2=[7,25,10,5]

cikar=[ sonuc  for sonuc in list(map(lambda x1,y1: x1-y1,list1,list2) ) if sonuc<0]
print(cikar)



#filter
letters=['a','b','d','e','i','j','o']

def filter_words(letter):
    vowels=['a','e','i','o','u']
    
    if letter in vowels:
        return True
    else:
        return False

filtered_words=list(filter(filter_words,letters))
print(filtered_words)


seq=[0,1,2,3,5,8,13]
result=list(filter(lambda x: x%2!=0,seq))
print(result)



def is_multiple_of_3(num):
    return num%3==0

numbers=[1,2,3,4,5,6,7,8,9,10]
result= list(filter(lambda x: is_multiple_of_3(x),numbers))
print(result)


numbers=range(1,50)

def is_prime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

asal=list(filter(is_prime,numbers))
print(asal)
    
    
             
