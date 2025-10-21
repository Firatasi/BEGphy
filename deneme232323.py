
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
    


numbers=[12,15,20,24,30,35,40,45,48,50,60,75]
#Soru: Bir liste halinde verilen sayıların
#sadece çift ve 3'e bölünebilen olanlarını
#filtreleyip,  bu sayıların karelerini hesaplayın.
#Hem filter hem de list comprehension kullanın

filtered_numbers= list(filter(lambda x: x%2 ==0 and x%3==0,numbers))

kare_al= [i**2 for i in filtered_numbers ]
print(kare_al)


kisiler=["Ali","Derya","Halime","Selim"]
tarihler=[1998,2002,2007,1967]
kisiler_tarihler= list(zip(kisiler,tarihler))
print(kisiler_tarihler)
             
filtrelenmis_kisiler= list(filter(lambda x:1998<= x[1] <=2007,
                                  kisiler_tarihler))
print(filtrelenmis_kisiler)


dosyalar=["data.csv","report.txt","image.png","notes.txt"
          ,"sunum.pptx","script.py"]

filtelenmis_dosyalar= list(filter(lambda x: x.endswith("txt"),
                                  dosyalar))
print(filtelenmis_dosyalar)


employees=[
    {'name':'AHMET','salary':90000,'department':'IT'},
    {'name':'Veli','salary':70000,'department':'Management'},
    {'name':'Ayşe','salary':60000,'department':'Finans'},
    {'name':'Yeşim','salary':50000,'department':'Marketing'},
    {'name':'AHMET','salary':50000,'department':'IT'}    
]

maas_filtrelenmis= list(filter(lambda x: x['salary']>60000
                               ,employees))
print(maas_filtrelenmis)


#Any Kullanımı

myList=[False,True,True]
x=any(myList)
print(x)

#All Kullanımı
mylist=[True,True,True]
mylist2=[False,True,True]
x=all(mylist)
y=all(mylist2)
print(x)
print(y)


#örnek1
#bir listede en az bir pozitif sayı
#olup olmadığını kontrol ediniz

numbers=[-1,-2,0,-5,3,-10]

positive_numbers=any( x>0 for x in numbers)
print(positive_numbers)


#listede tüm sayıların pozitif
#olup olmmadığını kontrol ediniz

kontrol= all( x>0 for x in numbers)
print(kontrol)


#bir listedeki stringlerin en az birinin boş
#olup olmadığını kontrol

strings=["merhaba","dünya", "python",""]

bos_var_mi= any(s==""  for s in strings)
print(bos_var_mi)


words=["elma","muz","vişne","hurma"]
alfabetik= all( w.isalpha() for w in words )
print(alfabetik)


sayilar=[33,44,66,77,88]
cift_mi=all(i%2==0 for i in sayilar)
print(cift_mi)


datam={
    'ad':'Volkan',
    'yas':24,
    'meslek':'Mühendis',
    'sehir':None
}
bos_mu= any(d==None for d in datam.values())
print(bos_mu)

#sorted fonksiyonu

#bir sayı listesini küçükten büyüğe sıralama

numbers=[23,1,45,78,3,12,56]

sorted_numbers=sorted(numbers)
print(sorted_numbers)


employees=[
    {'name':'AHMET','salary':90000,'department':'IT'},
    {'name':'Veli','salary':70000,'department':'Management'},
    {'name':'Ayşe','salary':60000,'department':'Finans'},
    {'name':'Yeşim','salary':50000,'department':'Marketing'},
    {'name':'AHMET','salary':45000,'department':'IT'}    
]

#çalışnalrı maaşlarına göre küçükten büyüğe sıralayalım
#sorted ile
sirali_maas= sorted(employees,key=lambda x: x['salary'])
print(sirali_maas)


numbers=[34,12,56,78,90,23,45]
min_num=min(numbers)
max_num=max(numbers)
print("min:",min_num)
print("max:",max_num)


list1=[10,50,30]
list2=[20,40,60]

min_values=list( map(min,list1,list2))

max_values= list(map(max,list1,list2))

print("min values: ",min_values)
print("max values: ",max_values)

#sum ve round

number=12.34567
rounded_num=round(number,3)
print(rounded_num)

numbers=[111,335,678,986]
print(sum(numbers))

ortalama =sum(numbers)/len(numbers)
print(ortalama)



#Uyg1: 
"""
Size aynı uzunlukta liste1 ve liste2 olmak üzere iki tamsayı listesi verildi. 
Aşağıdaki görevleri gerçekleştiren bir Python programı yazın:

Görev 1: liste1 ve liste2'nin karşılık gelen öğelerini toplamak için map fonksiyonunu 
kullanın.
Görev 2: List comprehension özelliğini kullanarak, toplam değeri 10 eşik 
değerinden küçük olan sonuçları filtreleyin.Yani onları almayın

Görev 3: Yalnızca 10'dan büyük olan toplamları içeren son listeyi döndürün.

list1 = [5, 3, 10, 15]
list2 = [4, 7, 1, 8]

"""
list1=[5,3,10,15]
list2=[4,7,1,8]

son_liste=[ i for i in  list(map(lambda x1,x2: x1+x2,list1,list2)) if i>10 ]
print(son_liste)



""" 
insanların isimlerini temsil eden dizelerden oluşan bir liste verildi. 
Aşağıdaki görevleri yerine getiren bir Python programı yazın:

Görev 1: Her ismin ilk harfini büyük yapmak için map fonksiyonunu kullanın 
(örneğin, 'john', 'John' olur).

Görev 2: Liste kavrama özelliğini kullanarak 3 karakterden az olan isimleri filtreleyin.
yani 3 ten az olanları almayın

Görev 3: 3 karakterden daha uzun olan büyük harfli isimlerin son listesini döndürün.

names = ['ahmet', 'mehmet', 'ali', 'ayşe', 'gül', 'serap']
"""

names = ['ahmet', 'mehmet', 'ali', 'ayşe', 'gül', 'serap']

son_ad=[ad for ad in      list(map(lambda x: x.capitalize(),names)) if len(ad)>3]
print(son_ad)

#uygulama3
"""
Bir liste içinde çeşitli sayıların bulunduğu bir Python listesi veriliyor. 
Sizden istenen, listenin yalnızca çift sayılarını alıp, bu sayıları
2 ile çarparak yeni bir liste oluşturmanızdır. 
Ayrıca, yeni listenin her elemanı için şunu kontrol etmelisiniz: 
Eğer sayı 10'dan büyükse, 
o sayının "Büyük" olarak değiştirilmesini, 
değilse sayının olduğu gibi kalmasını sağlayın.
Bu işlemi list comprehension ile yapın.
"""
numbers = [4, 7, 9, 12, 5, 2, 15, 8]

new_list = ["büyük" if i * 2 > 10 else i*2 for i in numbers if i % 2 == 0]
print(new_list)

#recursive
def faktoryel(n):
    if n==0:
        return 1
    else:
        return n* faktoryel(n-1)
print(faktoryel(5))
print(faktoryel(0))

#0, 1, 1, 2, 3, 5, 8, 13, .
def fibonacci(n):
    
    if n==0:
        return 0
      
    
    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5)) #yani kendinden önce gelen son 2 sayıyı topladı 
print(fibonacci(6))

##### fibonacci kodu doğru çalışıyor