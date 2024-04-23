# region example 5
# Kullanıcıdan alınan araç türü ve hız bilgisi üzerinden ceza var yada yok
#otomobil kamyon motorsiklet
# 50 30 60

# arac = input("araç ne?")
# hiz = int(input("aracın hızı?"))
#
# if hiz > 0:
#     if arac == "otomobil" :
#         if hiz >= 50:
#             print("cezalısın")
#         else:
#             print("cezalı değilsin")
#
#     elif arac == "motorsiklet" :
#         if hiz >= 60:
#             print("cezalısın")
#         else:
#             print("cezalı değilsin")
#
#     elif arac == "kamyon" :
#         if hiz >= 30:
#             print("cezalısın")
#         else:
#             print("cezalı değilsin")
#     else:
#         print("böyle bir araç yok")
#

# endregion

# region example 6
# kullanıcıdan alınan üç tane sayıdan büyük olanı ekrana yazın
#
# x = int(input("lütfen 1. sayıyı giriniz."))
# y = int(input("lütfen 2. sayıyı giriniz."))
# z = int(input("lütfen 3.sayıyı giriniz."))
#
# if x > y and x > z:
#     print(f'en büyük sayı {x} tir.')
# elif y > x and y > z:
#     print(f'en büyük sayı {y} dir.')
# elif z > x and z > y:
#     print(f'en büyük sayı {z} dir.')
# else:
#     print("sayıların hepsi birbirine eşittir.")

# endregion

# region example 7
#Kullanıcıdan aradığı ürün bilgsiini alıp hangi reyondaysa ona yolluyoruz

# ürün = input("Aradığınız ürün nedir?")
# #teknolohi sebze ve kozmetik
# #telefon kulaklık brokoli marul diş fırçası sabun
#
# if ürün == "kulaklık" or ürün == "telefon":
#     print("Gitmeniz gereken reyon teknoloji reyonudur.")
# elif ürün == "brokoli" or ürün == "marul":
#     print("Gitmeniz gereken reyon sebze reyonudur.")
# elif ürün == "diş fırçası" or ürün == "sabun":
#     print("Gitmeniz gereken reyon kozmetik reyonudur.")
# else:
#     print("Böyle bir ürün yok.")

# endregion


# region example 8

#kullanıcının satın aldığı kitap sayısını alalım
#bir kitap 5 tl
#1-20  arasında kitap alırsa % 5
#21 - 50  arasında kitap alırsa % 10
#51 - 75  arasında kitap alırsa % 15
#76 - 100  arasında kitap alırsa % 20

# sayi = int(input("Kaç kitap satın almak istiyorsunuz?"))
#
# if 1<= sayi <= 20:
#     ödeme = sayi * 5 * 0.95
#     print(f'tebrikler %5 indirim hakkınız var ödeyeceğiniz miktar {ödeme} dir')
# elif 21 <= sayi <= 50:
#     ödeme = sayi * 5 * 0.90
#     print(f'tebrikler %10 indirim hakkınız var ödeyeceğiniz miktar {ödeme} dir')
# elif 51 <= sayi <= 75:
#     ödeme = sayi * 5 * 0.85
#     print(f'tebrikler %15 indirim hakkınız var ödeyeceğiniz miktar {ödeme} dir')
# elif 76 <= sayi <= 100:
#     ödeme = sayi * 5 * 0.80
#     print(f'tebrikler %20 indirim hakkınız var ödeyeceğiniz miktar {ödeme} dir')
# else:
#     print("sen iyi misin dostum?")

#endregion

# region example 9
# linear bir doğrunun katsayılarını bulun
# delta = b** -4 * a * c
# delta sıfırdan büyükse iki kök
# delta sıfırsa 1 kök
# delta sıfırdan küçükse real kök yok
# from math import sqrt
#
# a = int(input("'a' sayısını giriniz."))
# b = int(input("'b' sayısını giriniz."))
# c = int(input("'c' sayısını giriniz."))
#
# islem = b ** 2 - 4 * (a * c)
#
# if islem > 0:
#     x1 = - b - sqrt(islem) / 2 * a
#     x2 = - b + sqrt(islem) / 2 * a
#     print(f'iki reel kök vardır. \nilk reel kök: {x1}\nikinci reel kök: {x2}')
# elif islem == 0:
#     x1 = - b - sqrt(islem) / 2 * a
#     print(f'Bir kök vardır. \nilk reel kök: {x1}')
# else:
#     print("reel kök yoktur.")

#endregion

# region example 10
#kullanıcı login olsun
#bmi bilgisi verelim

kullaniciAdi = input("Kullanıcı adınızı giriniz.")
sifre = input("Şifrenizi giriniz.")
#kullanıcı adı = brsttli
#şifre = sifrebrs

if kullaniciAdi == "brsttli" and sifre == "sifrebrs":
    print("Hoşgeldiniz.")
    boy = float(input("Lütfen boyunuzu metre cinsinden yazınız."))
    kilo = float(input("Lütfen kilonuzu KG cinsinden yazınız."))
    bmi = kilo / boy ** 2
    if 0 < bmi <= 18.5:
        print(f'Vücut kitle endeksiniz {bmi}. Bu değere göre çok zayıfsınız.')
    elif 18.5 < bmi <= 24.9:
        print(f'Vücut kitle endeksiniz {bmi}. Bu değere göre kilonuz normal')
    elif 25 <= bmi <= 29.9:
        print(f'Vücut kitle endeksiniz {bmi}. Bu değere göre kilolusunuz.')
    elif 30 <= bmi <= 34.9:
        print(f'Vücut kitle endeksiniz {bmi}. Bu değere göre obezsiniz.')
    elif 35 < bmi:
        print(f'Vücut kitle endeksiniz {bmi}. Yani yeme içme kardeşim enough aq.')
else:
    print("Kullanıcı adınız veya şifrenizde bir hatanız var. Lütfen tekrar deneyin.")


# endregion