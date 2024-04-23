
#Değer döndüren fonksiyonlar (Returnable)


#lst içerisindeki çift sayıları 2 ile çarparak lst_1 içerisine ekleyelim. Tek sayıları 3 ile çarparak lst_2'ye ekleyelim.
# lst = [12, 11, 19, 2 ,99]
# lst_1 = []
# lst_2 = []
#
# def tek_cift_mi(sayi: int):
#     if sayi % 2 == 0:
#         return "cift"
#     else:
#         return "tek"
#
# def append_list(result: str, sayi: int):
#     if result == "cift":
#         lst_1.append(sayi * 2)
#     else:
#         lst_2.append(sayi * 3)
#
# def main():
#     for i in lst:
#         result = tek_cift_mi(i)
#         append_list(result, i)
#     print(lst_1)
#     print(lst_2)
#
# main()

#Kullanıcıdan alınan 3 adet sayıyı topladıktan sonra karesini alarak sonucu ekrana yazdıralım.

# def toplam(s1: int, s2: int, s3: int):
#     return s1 + s2 + s3
#
# def karesini_hesapla(sayi: int):
#     print(f'Sonuç: {sayi ** 2}')
#
# def main():
#     x = int(input("Sayı: "))
#     y = int(input("Sayı: "))
#     z = int(input("Sayı: "))
#
#     sonuc = toplam(x, y, z)
#
#     karesini_hesapla(sonuc)
#
#     # karesini_hesapla(toplam(x, y, z)) # Yukarıdaki iki satırı bu şekilde yazabiliriz.
#
# main()


#Aşağıdaki listede bulunan rakamların liste içerisinde geçme sıklığını bulun ve sözlük tipinde çıktı verin rakamın kendisi key geçme sıklığı value olacak şekilde.
# rakamlar = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 4, 2, 2, 4, 3, 5, 1, 9]
#
# def frequency_count(numbers: list):
#     frequency_dictionary = {}
#
#     for item in numbers:
#         if item in frequency_dictionary:
#             frequency_dictionary[item] += 1
#         else:
#             frequency_dictionary[item] = 1
#
#     for key, value in frequency_dictionary.items():
#         print(f'Key: {key} - Value: {value}')
#
# frequency_count(rakamlar)


# Bir söz öbeğinde tekrar eden kelimelerden arındırarak çıktı verelim
# örnek input ==> merhaba ben burak burak ben burak
# Çıktı ==> merhaba ben burak


# def remove_duplicate_word(sentece: str):
#     lst = []
#
#     for item in sentece.split(' '):
#         if item not in lst:
#             lst.append(item)
#
#
#     result = ' '.join(lst)
#
#     print(result)
#
# cumle = input("please type something: ")
# remove_duplicate_word(cumle)


#kullanıcıdan alınan söz öbeğindeki kelimeleri alfabetik olarak sıralayalım

# def sort_word(sentece: str):
#     words = []
#     for item in sentece.split(" "):
#         words.append(item)
#
#     words.sort()
#
#     print(words)
#
# sort_word(input("Type something: "))


# Kullanıcı sign in sign up
# Kullanıcı isimleri aynı olmasın

user_dict = {
    "1": {
        "user_name": "beast",
        "password": "123"
    },
    "2": {
        "user_name": "savage",
        "password": "123"
    }
}

def sign_in(user_name: str, password: str):
    is_active = False

    for i in range(1, len(user_dict) + 1):
        if user_dict.get(str(i)).get("user_name") == user_name and user_dict.get(str(i)).get("password") == password:
            is_active = True
            break

    if is_active:
        print("Welcome")
    else:
        print("Invalid credantial")


def get_user_name(users: dict):
    user_name_list = []

    for i in range(1, len(users) + 1):
        user_name = users.get(str(i)).get("user_name")
        user_name_list.append(user_name)

    return user_name_list


def sign_up(user_name: str, password: str):
    if user_name in get_user_name(user_dict):
        print("Invalid user name. Please choose a different user name..!")
    else:
        user_dict[len(str(user_dict)+1)] = {
            "user_name": user_name,
            "password": password
        }

        print("Your password has created.")

def main():
    while True:
        process = input("Type a process: ").lower()

        if process == "exit":
            print("Application has been closing..!")
            break
        elif process == "sign in":
            user_name = input("User Name: ")
            password = input("Password: ")
            sign_in(user_name, password)
        elif process == "sign up":
            user_name = input("User Name: ")
            password = input("Password: ")
            sign_up(user_name, password)
        else:
            print("Please type a valid provess..!")

main()