class ABC :
    def __init__(self,language,letter):
        self.language=language
        self.letter=letter

class EnglishABC(ABC):
    def __init__(self, number_of_letters,letter,language):
        super().__init__(self, language)
        self.number_of_letters=number_of_letters
        self.language=language
        self.letter=letter

def getabs():
    letter=[ "А", "Б", "В", "Г", "Ґ","Е", "Є", "Ж", "З", "И", "І", "Ї",
             "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
             "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я" ]

    temp=ABC(language="UKR",letter=letter)
    return temp
def getenglishABC():
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    temp1=EnglishABC(number_of_letters="26",language="ENG",letter=letter)
    return temp1
def print_all_letter(list):
      print(list)

def text():
     print("Hellow World")

def count_of_letter(list):
    return print(len(list))

def check(b):
     temp=input("Ведіть будь яку букву\n")
     if  temp == b.letter:
         print("Належить літера до англійської абетки")
     else:
         print("Не належить до англійської абетки ")

def print_menu():
    print("1 - Надрукувати всі букви алвафіту ")
    print("2 - Порахувати кількість букв  ")
    print("3 - Чи належить літера до англійської абетки ")
    print("4 - Текст анлійською мовою ")
    print("Для завершення введіть 0")

print ("Виберіть дію")
print_menu()
choice = int(input())

while choice != 0:
    if choice == 1:
       temp=getabs()
       print_all_letter(temp.letter)
       print_menu()
       choice = int(input())
    elif  choice == 2:
        print("В якій мові ви хочете порахувати кількість букв\n 1 - Ukr \n 2 - Eng ")
        choice1 = int(input())
        if choice1 == 1:
            temp= getabs()
            count_of_letter(temp.letter)
            print_menu()
            choice = int(input())
        elif choice1 == 2:
           temp=getenglishABC()
           print(temp.number_of_letters)
           print_menu()
           choice = int(input())
    elif choice == 3:
        b = getenglishABC()

        check(b)
        print_menu()
        choice = int(input())
    elif choice == 4:
        text()
        print_menu()
        choice = int(input())