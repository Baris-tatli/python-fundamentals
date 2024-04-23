#
#
# Dictionary (Sözlük)
# Sözlük, List, tuple gibi bir başka verileri depoladığımız yapıdır.
# Sözlükler anahtar ve değer (key & value) mantığında çalışırlar.

# my_dict = {
#     "Full Name": "Burak Yılmaz",
#     "Age": 34,
#     "Interested Sport": {"Boxing", "wrestling", "UFC"},
#     "Favorite Books": {
#         "war history": "Cambridge war History",
#         "Scientfic:": {
#             "Karl Poper": "The Logic Scientifc Fiscovery"
#         }
#     }
# }

# release_year_movie = {
#     "fight club": 1999,
#     "the matrix": 1999,
#     "Interstaller": 2014,
#     "Inception": 2010,
#     "dune": 2011
# }
#
#
# # Herhangi bir value ekrana basın.
# #
# # #yol 1
# # print("Inception filminin çıkış yılı:", release_year_movie["Inception"])
# #
# # #yol 2
# # print(f'Interstaller Relase: {release_year_movie.get("Interstaller")}')
# # print(f"The matrix çıkış tarihi: {release_year_movie.get('the matrix')}")
# #
# # Sözlüğün tüm anahtarlarını ekrana yazdırın
# for key in release_year_movie.keys():
#     print(key)
# # Sözlüğün tüm valuelarını ekrana yazdırın
# for value in release_year_movie.values():
#     print(value)
# # Sözlüğün tüm itemlerini ekrana yazdırın
# print(release_year_movie.items())
# for key, value in release_year_movie.items():
#     print(f'movie name: {key}\n'
#           f'release year: {value}')

# CRUD (Create-Read-Update-Delete)
# products = [
#     {"name": "everlasst pro boxing gloves", "price": 245},
#     {"name": "everlasst training gloves", "price": 200},
#     {"name": "everlasst heavy bag", "price": 445},
#     {"name": "Iphone 15 pro max", "price": 85000},
#     {"name": "samsung s24 ultra", "price": 80000},
#     {"name": "Lenovo x1 carbon", "price": 59000},
#     {"name": "Regal Raptor DD 150 e2-F", "price": 55000},
# ]

#product listesindeki tüm ürünlerin fiyatlarını toplayarak ekrana yazın.

# total_price = 0
# for product in products:
#     # print(product.get("price"))
#     total_price += product.get("price")
# print(f'Total Price: {total_price}')

#products listesindeki ürünlerin fiyatı 30000'den büyük olan ürünleri listeleyin

# total_price = 0
# for product in products:
#     x = (product.get("price"))
#     if x >= 30000:
#         print(f'30 bin liraya eşit veya daha fazka fiyatı olan ürünlerden;\nName: {product.get("name")}\nprice: {product.get("price")}')

# ürün adı içerisinde everlast geçen ve fiyat aralığı 240 ile 500 arasomda olan ürünleri listeleyiniz.
# for product in products:
#     if product.get("name").__contains__("everlasst"):
#         if 240 <= product.get("price") <= 500:
#             print(f'Belirlediğiniz kriterlerdeki ürünler;\nName: {product.get("name")}\nPrice: {product.get("price")}')
#         else:
#             pass
#     else:
#         pass

#boş bir students sözlüğü yaratalım
#Dictionary Syructure
#students


# student = {
#     'student_id': {
#         'first_name': 'Barış',
#         'last_name': 'Tatlı',
#         'phone': '05416035744'
#     },
#     'student_id0': {
#         'fşrst_name': 'Olcay',
#         'last_name': 'Arslan',
#         'phone': '05317898737'
#     }
# }
#
# #Öğrenci id'lerini uuid4 ile yaratın.
# from uuid import uuid4
# from pprint import pprint
# students = {}
# while True:
#     print('Manuel Guide\n'
#           '============\n'
#           'Create\n'
#           'Update\n'
#           'Delete\n'
#           'Exit\n')
#     process = input("Type your provess upon manuel guide: ").lower()
#
#     match process:
#         case 'create':
#             student_id = str(uuid4())
#             first_name = input("first name: ")
#             last_name = input("last name: ")
#             phone = input("phone: ")
#             students[student_id] = {
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'phone': phone
#             }
#         case 'list':
#             print(students)
#         case 'update':
#             student_id = input("type id: ")
#             first_name = input("first name: ")
#             last_name = input("last name: ")
#             phone = input("phone: ")
#
#             students.update({
#                 student_id: {
#                     'first_name': first_name,
#                     'last_name': last_name,
#                     'phone': phone
#                 }
#             })
#         case 'delete':
#             student_id = input("type id: ")
#             del students[student_id]
#             print(f'{student_id} has been removed..')
#         case 'exit':
#             print('Application has been closing..!')
#             break
#         case _:
#             print("Please type valid process name..!")
 #bu en sonki örneğin product olanı yap

product = {
    "Product1": {
        "name": "İphone 15",
        "price": 55000
    }
}

from uuid import uuid4
from pprint import pprint
products = {}

while True:
    print('Manuel Guide\n'
          '============\n'
          'Create\n'
          'Update\n'
          "List\n"
          'Delete\n'
          'Exit\n')
    process = input("Yapmak istediğiniz işlemi seçin: ").lower()

    match process:
        case "create":
            product_id = str(uuid4())
            product_name = input("Product Name: ")
            product_price = int(input("Product Price: "))
            products[product_id] = {
                "name": product_name,
                "price": product_price
            }
        case "update":
            product_id = input("type id: ")
            product_name = input("Product Name: ")
            product_price = int(input("Product Price: "))
            products.update({
                product_id: {
                    "name": product_name,
                    "price": product_price
                }
            })
        case "list":
            print(products)
        case "delete":
            product_id = input("Type id: ")
            del products[product_id]
            print(f"{product_id} has removed")
        case "exit":
            print("Programdan çıkış yapılıyor.")
            break
        case _:
            print("Lütfen geçerli bir işlem giriniz.")
            pass