# While loop
# Tekrarlı işlemleri yaptırmak istediğimiz zaman tercih ettiğimiz bir mekanizmadır.
# While loop bir sayaç ile birlikte bir karar mekanizmasına sahip yapıdır. Sayaç arttırılıp yada azaltılarak her defasında şarta bakılıp şart tuttuğu sürece döngünün dönmesi temin edilir.


# sayac = 0
# while sayac < 100:
#     business Logic
#     sayac += 1

#region Example 1
# 0 ile 10 arasındaki sayıları ekrana yazdıralım.
# sayac = 0
# while sayac <= 10:
#     print(sayac)
#     sayac += 1
#endregion

#region Example 2
# 1 ile 100 arasındaki sayıları toplayarak sonucu ekrana yazdıralım
# sayac = 1
# toplam = 0
# while sayac <= 100:
#     toplam = toplam + sayac
#     sayac += 1
# print(f'toplam: {toplam}')
#endregion

#region Example 3
# 1 ile 100 arasındaki 100 dahil sayıları çift ve tek sayıların toplamlarını ayrı ayrı bularak ekrana yazdıralım.
# sayac = 1
# toplamTek = 0
# toplamCift = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         toplamCift = toplamCift + sayac
#     elif sayac % 2 == 1:
#         toplamTek = toplamTek + sayac
#     sayac += 1
#
# print(f'Tek sayıların toplamı: {toplamTek}')
# print(f'Çift sayıların toplamı: {toplamCift}')
#endregion

#region Example 4

# 0 ile 100 arasındaki 100 dahil sayılardan kaç tanesi çift kaç tanesi tek bunu ekrana yazdıralım.

# sayac = 0
# tek = 0
# cift = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         cift += 1
#     elif sayac % 2 == 1:
#         tek += 1
#     sayac += 1
#
# print(f'Toplam {tek} tane tek sayı vardır.')
# print(f'Toplam {cift} tane çift sayı vardır.')

#endregion

#region Example 5
# Kullanıcıdan işlem türü alıyoruz (e, +, -, *, /) alalım. Alınan işlem türüne göre ilgili işlemi yapalım ve çıktısını ekrana yazdıralım. Kullanıcı 'e' işlemini gönderene kadar sınırsız sayıda 4 işlem yapabilsin
# while True:
#     sayi0 = int(input("Lütfen ilk sayıyı giriniz."))
#     sayi1 = int(input("Lütfen ikinci sayıyı giriniz."))
#
#     toplama = sayi0 + sayi1
#     cikarma = sayi0 - sayi1
#     carpma = sayi0 * sayi1
#     bolme = sayi0 / sayi1
#
#     islem = str(input("Lütfen yapmak istediğiniz işlemi seçiniz.(toplama, çıkarma, çarpma, bölme veya programdan çıkmak için 'e')"))
#     if islem == "toplama":
#         print(toplama)
#     elif islem == "çıkarma":
#         print(cikarma)
#     elif islem == "çarpma":
#         print(carpma)
#     elif islem == "bölme":
#         print(bolme)
#     elif islem == "e":
#         break
#     else:
#         print("Yanlış tuşa mı bastın")
#endregion

#region Example 6
#Kullanıcıdan alınan sayı asal mı değil mi?

# sayi = int(input("Sayı giriniz: "))
#
# if sayi <= 0:
#     print("Sıfır ve negatif sayılar asal değildir.")
# else:
#     asal_mi = True
#
#     if sayi == 1:
#         asal_mi = False
#
#     sayac = 2
#     while sayac < sayi:
#         if sayi % sayac == 0:
#             asal_mi = False
#             break
#
#         sayac += 1
#
#     if asal_mi:
#         print(f'{sayi} asaldır.')
#     else:
#         print(f'{sayi} asal değildir.')

#endregion

#region Example 7
#Kullanıcıdan alınan sayının faktöriyelini hesaplayalım.
# sayi = int(input("Sayı giriniz."))
#
# if sayi < 0:
#     print("Negatif sayıların faktöriyeli hesaplanmaz.")
# elif sayi == 0 or sayi == 1:
#     print("faktöriyel 1'dir.")
# else:
#     sonuc = 1
#
#
#     while sayi > 0:
#         sonuc *= sayi
#
#         sayi -= 1
#
#     print(f'Sonuç: {sonuc}')

#endregion