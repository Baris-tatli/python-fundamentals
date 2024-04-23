

# File I/o
#Dosya açma ve kapama ve üzerinde CRUD işlemleri yapabileceğimiz bize fonksiyonlar tanımlayan file modüşü ile çalışacağız.

# #Dosya açma
# file = open(file="new_file.txt", mode="w", encoding="utf-8")
# file.write("Full Name: Barış Tatlı\nOccupation: Developer")
# file.close()
#
# #Yukarıda yaratılan dosya üzerine yeni bir kayıt ekleyelim.
# file = open(file="new_file.txt", mode="a", encoding="utf-8")
# file.write("\nLanguage: Phyton")
# file.close()
#
# #dosyadan veri okuyalım
# file = open(file="new_file.txt", mode="r", encoding="utf-8")
# for line in file.readlines():
#     print(line)


#region Task 1
#exam_grades.txt dosyasını yaratın
def create_exam_grades():
    file = open(file="exam_grades.txt", mode="w", encoding="utf-8")
    file.close()
#endregion

#region Task 2
#Kullanıcıdan first_name, last_name, midterm, final, homework bilgilerini alarak exam_grades.txt dosyasına yazalım.
#Asağıdaki formaya yazalım.
#Burak Yılmaz: 30,30,30
#ilgili dosyayı with open() kullanarak açalım
def take_information(first_name: str, last_name: str, midterm: float, final: float, homework: float):
    with open(file="exam_grades.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{first_name} {last_name}:{midterm},{final},{homework}\n")
#endregion

#region Task 3
#row example => Burak Yılmaz: 30,30,30
# def calculate_grade(row: str)-> str:
#     return "harf notu"

def calculate_grade(row: str)-> str:
    values = row.split(":")
    full_name = values[0]
    grades_list = values[1].split(",")

    ort = float(grades_list[0]) * 0.3 + float(grades_list[1]) * 0.6 + float(grades_list[2]) * 0.3

    if 90 <= ort <= 100:
        return f"{full_name}: AA"
    elif 85 <= ort <= 89:
        return f"{full_name}: BA"
    elif 80 <= ort <= 84:
        return f"{full_name}: BB"
    elif 75 <= ort <= 79:
        return f"{full_name}: CB"
    elif 70 <= ort <= 74:
        return f"{full_name}: CC"
    elif 65 <= ort <= 69:
        return f"{full_name}: CF"
    elif 60 <= ort <= 64:
        return f"{full_name}: DC"
    elif 55 <= ort <= 59:
        return f"{full_name}: DD"
    elif 50 <= ort <= 54:
        return f"{full_name}: FD"
    else:
        return f"{full_name}: FF"

#endregion


#region Task 4
#exam_grades.txt dosyasından verileri satır satır okuyalım
#harf notlarını hesaplatalım ve bir listeye ekleyelim
#ilgili listeyi return edelim
#örnek return => lst = ["Burak Yılmaz: FF", "Hakan Yılmaz: AA"]
def read_exam_grades() -> list:
    lst = []
    with open(file="exam_grades.txt", mode="r", encoding="utf-8") as file:
        for row in file:
            grade = calculate_grade(row)
            lst.append(grade)

    return lst
#endregion

#region Task 5
#result.txt isimli dosyaya öğrencilerin isim soyisim harf notunu yazzdıralım
def register_grade(grades_list: list):
    with open(file="result.txt", mode="w", encoding="utf-8") as file:
        for item in grades_list:
            file.write(item + "\n")
#endregion

#region Tastk 6
#result.txt dosyasının verilerini ekrana bas
def read_result():
    with open(file="result.txt", mode="r", encoding="utf-8") as file:
        for row in file:
            print(row)
#endregion

def menu():
    print(f"""
    Menu
    =====================
    Read Grades      => 1
    Enter Grades     => 2
    Calculate Result => 3
    Read Result      => 4
""")

def main():
    menu()

    while True:
        process = input("Please choose a transaction: ")

        match process:
            case "1":
                read_exam_grades()
                print("Grades has been read..!")
            case "2":
                take_information(
                    input("First Name: "),
                    input("Last Name: "),
                    float(input("Midterm: ")),
                    float(input("Final: ")),
                    float(input("Homework: ")),
                )
            case "3":
                result = read_exam_grades()
                register_grade(result)
                print("Grades have been calculated and stored..!")
            case "4":
                read_result()
            case "e":
                print("Application has been closing..!")
                break
            case _:
                print("Please choose a valid transaction no..!")

main()