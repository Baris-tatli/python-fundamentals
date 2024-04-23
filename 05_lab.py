

#List
# Uygulama içerisinde anlık olarak bizim bir yada birden fazla değer tutan yapılardır. Farklı tiplerde değerler tutabilirler. Listelerde RAM üzerinde ...... alanında tutulduğu için değişkenler gibi uygulama sonlandığında RAM'dan uçurulurlar yani Run Time (uygulama çalışırken) içerisine eklenilen değerleri Hard Disk gibi ssaklayamazlar.

# Liseler index mantığı ile çalışırlar. Liste içerisinde saklanılan değerler sıfırıncı index'ten başlayarak pozitif yönde artan index değerlerinde depolanırlar. Yani 1. index'te tutulan değere ulaşmak için index değerini yani 1 kullanabilirim.

# top_boxers = ["Mike Tyson", "Muhammed Ali", "Lenox Lewis", "Evander Holyfield", "Rocky Marciano"]
# print(top_boxers[0])


#region task 1
# Georgre forman bilgisiniz top_boxers listesinin sonuna ekleyelim

# top_boxers.append("George Foreman")
# print(top_boxers)

#endregion


#region task 2
#Antony jasua bigisini top_boxers listesinin 4. indexine ekleyelim.

# top_boxers.insert(4, "Antony Jasua")
# print(top_boxers)

#endregion


#region task 3
#Antony jasua bigisini top_boxers listesinden silelim.

# top_boxers.remove("Antony Jasua")
# print(top_boxers)

#endregion


#region task 4
#5. indexteki bigiyi top_boxers listesinden silelim.

# top_boxers.pop(5)
# print(top_boxers)

#endregion

#region task 5
# aşağıdaki curreny_boxers listesi ile top_boxers listesini birleştirelim.

# current_boxers = ["Antony Jasua", "Tyson Fury", "Deantony Wilder"]
# top_boxers.extend(current_boxers)
# print(top_boxers)

#endregion

#region task 6
#sayılar isimli bir liste içerisine otomatik olarak random 10 tane sayı ile dolduralım

# from random import randint
# sayiListesi = []
# for i in range(10):
#     #yol 1
#     randomUret = randint(0, 1000)
#     sayiListesi.append(randomUret)
#     #yol 2
#     # sayiListesi.append(randint(0, 1000))
# print(sayiListesi)

#endregion

#region task 7
# Kullanıcıdan bir söz öbeği alalım. Örneğin "Merhaba ben Barış Tatlı"
# Kullanıcıdan alınan söz öbeğindeki tüm harfleri küçük harflere dönüştürün
# İlgili söz öbeğindeki sesli harfleri, sesli harfler listesine.
# Sessiz harfleri ise sessiz harfler listesine ekleyelim.
# örneğin e harfi ilgili listeye eklendiyse bir daha eklemeyelim.
# Rakam girildiyse onları eleyin

# list = input("Bir cümle giriniz.").lower()
# sesli_harfler_listesi = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
# sesli_harfler = []
# sessiz_harfler = []
# for i in list:
#     if i.isalpha(): # isalpha() built-in fonksiyonu ilgili karakter a-z yada A-Z harf aralığında mı diye bakar.
#         if i not in sesli_harfler and i not in sessiz_harfler:
#             if i in sesli_harfler_listesi:
#                 sesli_harfler.append(i)
#             else:
#                 sessiz_harfler.append(i)
#
# print(sesli_harfler)
# print(sessiz_harfler)

#endregion

#region task 8
# İki listeyi random sayilarla dolduralım.
# Akabinde benzer indexlerde tutulan değerleri toplayarak 3. listede yine aynı index ise yazdıralım

# from random import randint
# sayiListesi1 = [] #boş liste
# sayiListesi2 = [] #boş liste
# toplamListesi = [] #boş liste
# for i in range(10):
#     #yol 1
#     randomUret = randint(0, 1000) #0 ile 1000 arasında sayı üretir.
#     sayiListesi1.append(randomUret) #boş "sayiLisetesi1" listesine üretilen sayıyı koyar
#
#     randomUret1 = randint(0, 1000) #0 ile 1000 arasında sayı üretir.
#     sayiListesi2.append(randomUret1) #boş "sayiLisetesi2" listesine üretilen sayıyı koyar
#
#     islem = randomUret + randomUret1 # randomUret değişkeninde bulunan rastgele sayı ile randomUret1 değişkenindeki sayıları toplayıp islem değişkenine atar.
#
#     toplamListesi.insert(i, islem) #Boş olan toplamListesine toplanan sayıyı yazar.
#
#
# print(sayiListesi1) #10 tane 0 ile 10000 arasında rastgele 10 tane sayının listesi
# print(sayiListesi2) #10 tane 0 ile 10000 arasında rastgele 10 tane sayının listesi
# print(toplamListesi) #Toplanan sayıların listesi

#endregion

#region task 9
# users listesi içerisinde bulunan kullanıcılara kurumsal mail adresi oluşturalım
# örneğin burak.yilmaz@bilgeadam.com
# users = ['burak yilmaz', ' ertuğrul', 'bora eren erdem', 'kerim abdul cabbar okkes', ' ']
mail_address = []
users = []

#kullanıcıdan isim ve soyisim bilgilerini alalım.
user_name = str(input("İsminizi giriniz.")).lower()
user_surname = str(input("Soyisminizi giriniz.")).lower()

#users listesine kullanıcının isim ve soyismini ekleyelim
users.append(user_name)
users.append(user_surname)

#kullanıcıya mail adresinin oluşturulduğunu kullanıcıya belirtelim ve bu mail adresini mail_adress listesine ekleyelim.
print("Mail adresiniz otomatik olarak oluşturuldu.")
mail_address.append(f"{user_name}.{user_surname}@bilgeadam.com")

# Kullanıcının girdiği password is valid mi?
# 1. girilen şifre en az 16 karekter uzunluğunda olmalı
# en az bir büyük bir küçük harf olmalı
# en az bir rakam olmalı
# en az bir tane noktalma işareti olmalı
# her hangi bir ifade tekrar etmemli

import string

user_password = input("Lütfen bir şifre belirleyiniz(Şifreniz en az 16 karakter uzunluğunda, en az bir büyük bir küçük harf, en az bir rakam ve en az bir noktalama işareti içermelidir.)")
#sorgulayacağımız kriterleri yazalım
buyuk_harf = any(char.isupper() for char in user_password)
kucuk_harf = any(char.islower() for char in user_password)
rakam_varmi = any(char.isdigit() for char in user_password)
noktalama_varmi = any(char in string.punctuation for char in user_password)

#kriterleri sorgulayalım ve buna göre bir çıktı verelim.
if buyuk_harf and kucuk_harf and rakam_varmi and noktalama_varmi and len(user_password) == len(set(user_password)):
    print("Şifreniz belirlendi ve kaydedildi.")
else: print("Lütfen belirlediğiniz şifrenizin tüm kriterlere uyup uymadığını kontrol ediniz.")

print(f'Mail adresiniz: {mail_address}\nŞifreniz: {user_password}')


#endregion

