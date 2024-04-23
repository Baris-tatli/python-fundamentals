# Try - Except - Finally
# Uygulamalarda anlık olarak alınan hatalara (exception) yani istisnai durumlar diyoruz. Bu durumları try - except blokları ile handle etmeye çalışıyoruz.

# try :
#     x = int(input("Tam sayı giriniz: "))
#     sonuc = x / 0
#     print(sonuc)
# except ZeroDivisionError as problem:
#     print(f"Bir tam sayı sıfıra bölünmez knkss.\n{problem}")
# finally:print("N'olursa olsun ben çalışırım arkadaş.")

try:
    age = int(input("Age: "))
    print(age)
except ValueError as problem:
    print(f'{problem}')
else:
    print("exception çalışmazsa çalışır.")
finally:
    print("ne olursa çalışırım.")