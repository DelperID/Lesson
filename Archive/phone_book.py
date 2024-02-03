# В данном скрипте пробую сделать базу данных типа телефонной книги

# numbers- это переменная, в нее можно разместить что угодно, любой тип данных. В данном случае это телефонна книга, где есть 1 ключ и 1 значение на строчку. "Dmitry"- является ключом, а "+7123456789" его значением
numbers = {
    "Dmitry": "+7123456789",
    "Konstantin": "+7123321221"
}

name = input("What is your name?")
number = numbers.get(name)
if number is None:
    print("Sorry, but your name is not in... ")
else:
    print(number)

# name= input("What is your name?")
# print(numbers[name])
