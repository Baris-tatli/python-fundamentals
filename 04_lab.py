# FOR LOOP
# For loop'a geçmeden önce incelememiz gereken yardımcı fonksiyon ve operatör bulunmaktadır. Bunlar "in" ve "not in" ayrıca range () built-in fonksiyondur.

# "in" ve "not is"
# name = "Barış Tatlı"
#not  : string ifadeler karakter listeleridir.

# print(' ' in name) #output => True
# print('b' in name) #output => False
# print('a' in name) #output => True
# print('B' in name) #output => Truee
#
# # not in operatörü
# print('z' not in name) #output => True
# print(' ' not in name) #output => False
# print('a' not in name) #output => False

# Not: fonksiyonların içerisine verdiğimiz argümanlara göre fonksiyonlar farklı işler icra ederler. Burada farklı işlerden kastımız birbirinden alakasız işlemler değildir. Ana bir iş mantığının faklı versiyonlarıdır. Aşağıdaki range fonksiyonunu bu cümleye göre inceleyelim.
# range() => range fonksiyonunun ana iş mantığı bize bir sayı listesi dönmesidir. Range aldığı argümanlara göre farklı sayı listeleri yaratır.
# Bir argüman aldığında  => default olarak 0'dan başlayarak argüman olarak verilen tam sayı (n-1) olarak bir tam sayı listesi döner. Artış miktarı 1'dir.

# for i in range(10):
#     print(i, end = "-")

# 2 argüman aldığında => range(10, 20), bu durumda 10'dan başlayıp 19'a kadar tam sayı listesi döner. Artış miktarı 1'dir.

# for i in range(10, 20):
#     print(i, end = " ")

# 3 argüman alındığında => range(10, 101, 5), bu durumda 10'dan  başlayıp 100'e kadar 5'er 5'er artacak bir tam sayı listesi oluşturur.

# for i in range(10, 101, 5):
#     print(i, end = ",")

#region Example 1

#0 ile 100 arasındaki çift ve tek sayıların toplamlarını ayrı ayrı ekrana yazdıralım
# ciftlerinToplami = 0
# teklerinToplami = 0
# for i in range(0, 101):
#     if i % 2 == 0:
#         ciftlerinToplami += i
#     else:
#         teklerinToplami += i
# print(f'Çift sayıların toplamı: {ciftlerinToplami} ve tek sayıların toplamı: {teklerinToplami}')

#endregion

#region Example 2
#Başlangıç, bitiş ve artış miktarını kullanıcının belirlediği bir range() fonksiyonundaki her bir sayının karesini hesaplayarak ekrana yazdıralım

# x = int(input("Başlangıç sayınızı giriniz."))
# y = int(input("Bitiş sayınızı giriniz."))
# z = int(input("Artış miktarı için sayınızı giriniz."))
#
# for i in range(x, y, z):
#     islem = i * i
#     print(f"{i} sayısının karesi {islem}'dir")

#endregion

#region Example 3
#faktöriyel hesaplayalım.
# sayi = int(input("Sayı giriniz."))
# islem = 1
#
# if sayi < 0:
#     print("Negatif sayıların faktöriyeli hesaplanmaz.")
# elif sayi == 0 or sayi == 1:
#     print("faktöriyel 1'dir.")
# else:
#     for i in range(1, sayi + 1, 1):
#         islem = i * islem
#     print(f'{sayi} sayısının faktöriyelinin sonucu {islem}"dır.')
#endregion

#region Example 4
#Çarpım tablosu yap.
# for i in range(1, 11):
#     for j in range(1, 11):
#         islem = i * j
#         print(f'{i} * {j} = {islem}')

#endregion

#region Example 5
#içi '#' dolu dikdörtgen yapalım
# for i in range(5):
#     for j in range(20):
#         print('x', end="")
#     print(" ")

#endregion

#region Example 6
#içi dolu bir dik üçgen yapalım

# for i in range(10):
#     for j in range(10):
#         if j <= i:
#             print('x', end="")
#
#     print(" ")

#endregion