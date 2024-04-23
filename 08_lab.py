# CUSTON FUNCTİONS
# Bu zamana kadar python içerisinde built-in olarak bulunan fonksiyonlardan faydalandık. Örneğin range(), print(), randit() vb. bu fonksiyonlar onların üzerlerine atanmış işleri bıkmadan usanmadan yerine getiriyorlardı. Aldıktalı argümanlara göre üzerlerine yüklenen işleri değiş varsayanlarını yerine getiriyorlardı. Örneğin range() 2 argüman ve 3 argüman alması arasındaki fark gibi. Bizimde yazdığımız custom fonksiyonlar tamamen yukarıda bahsettiğim hususlara göre çalışacaklar.

# Declare a Function (Fonksiyon Tanımlama)
# def Function_name():
#     business logic


# Call a Function (Fonksiyonu kullanma)
# function_name()

#
# def greeting_people():
#     print("hello people")
#
# greeting_people()
#
# def sum_two_number(x: int, y:int):
#     """
#     This Function sum two numbeers.
#     :param x: it is must be integar
#     :param y: it is must be integar
#     :return: none
#     """
#     print(f'{x} + {y} = {x + y}')
#
# sum_two_number(
#     int(input("Number: ")),
#     int(input("Number: "))
# )


# alınan sayı çift mi tek mi?

# def sayi_kontrol(x: int):
#     """
#     program sayının çift veya tek olup olmadığını sorgular ve yanıtlar.
#     :param x: x integar olmak zorunda
#     :return: none
#     """
#     if x % 2 == 0:
#         print(f'{x} sayısı çifttir.')
#     elif x % 2 == 1:
#         print(f'{x} sayısı tektir.')
#     else:
#         print("sayı girmediniz.")

# sayi_kontrol(
#     int(input("Number: "))
# )

# kullanıcıdan full name alalım. burak.yilmaz@bilgeadam.com mail oluşturalım

# def mail_olustur(ad: str):
#     ayriltirilmis_ad = ad.lower().split(" ")
#     print(f'{ayriltirilmis_ad[0]}.{ayriltirilmis_ad[-1]}@bilgeadam.com')
#
# mail_olustur(
#     ad = str(input("Full Name: "))
# )

# kullanıcıdan alınan bir sayıyla faktöriyel alalım.

# def faktoriyel(x: int):
#     if x < 0:
#         print("Sıfırdan küçük sayıların faktöriyeli hesaplanmaz.")
#     else:
#         result = 1
#         if x == 0 or x == 1:
#             print(f'Sonuç: {result}')
#         else:
#             while x > 1:
#                 result *= x
#                 x -= 1
#             print(f'Sonuç: {result}')
#
# number = int(input("Number: "))
# faktoriyel(number)

#users = [("beast", "123"), ("bear", "234"), ("savage", "987"), ("brsttli", "brs44*")]
#kullanıcıdan user name ve password alalım login işlemi yapalım.
#users = [("beast", "123"), ("bear", "234"), ("savage", "987"), ("brsttli", "brs44*")]

# def login(user_name: str, password: str, user_list: list):
#     is_active = False
#     for username, pwd in user_list:
#         if username == user_name and pwd == password:
#             is_active = True
#             break
#
#     if is_active:
#         print("Hoşgeldiniz..")
#     else:
#         print("bilgileriniz yanlış...")
#
# kullanici_adi = input("Kullanıcı Adı: ")
# sifre = input("Şifreniz: ")
# login(user_name=kullanici_adi, password=sifre, user_list=users)

#lab 8 de yaptığımız örneği fonksiyonlar halinde tekrar yapın.
#create_student(), list_students(), update_student(), delete_student()
from uuid import uuid4
from pprint import pprint
students = {}

def create_student(first_name: str, last_name: str, phone: str):
    student_id = str(uuid4())
    students[student_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }

def update_student(student_id: str, first_name: str, last_name: str, phone: str):
    students.update({
        student_id: {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone
        }
    })

def delete_student(student_id: str):
    del students[student_id]
    print(f'{student_id} has been removed..')




while True:
    print('Manuel Guide\n'
          '============\n'
          'Create\n'
          'Update\n'
          'Delete\n'
          'Exit\n')
    process = input("Type your provess upon manuel guide: ").lower()

    match process:
        case 'create':
            first_name = input("first name: ")
            last_name = input("last name: ")
            phone = input("phone: ")
            create_student(first_name, last_name, phone)
        case 'list':
            print(students)
        case 'update':
            update_student(input("type id: "),
                           input("first name: "),
                           input("last name: "),
                           input("phone: "))
        case 'delete':
            student_id = input("type id: ")
            delete_student(student_id)
        case 'exit':
            print('Application has been closing..!')
            break
        case _:
            print("Please type valid process name..!")