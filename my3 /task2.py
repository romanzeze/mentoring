def palidrome(text):
    if text == text[::-1]:
        print("Слово", text[::-1] , "є палінромом ")
    else:
        print("Слово", text, "не є паліндром")

text=input("ведіть текст\n")
palidrome(text)

