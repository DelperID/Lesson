# x = [13, 2]
#
# if x == 0:
#     x = 1
#     print("x был равен нулю")
#
# elif type(x) == type(5) or type(x) == type(5.2):
#     print("x допустимое значение ")
#
# else:
#     print("Недопустимый тип данных в переменной \"x\" ")
#     x = 1 # Данная строка переприсваивает значение переменной Х на 1 в случае, если значение переменно Х не прошло проверку ни одним из условий (условными операторами if, elif and else)
#
# print(100/x)

first_guest = True
while True:
    if first_guest == True:
        print("Добро пожаловать в наш бар \"Серый Единорог!\" \nЛучший бар в городе Ороксдор! \nЕдинственное прибежище для любого орка, гнома или дворфа на континенте Эралорн. ")
    x = input("Сер, мне не видно вашего лица, к какой рассе вы относитесь?\n1 - Эльф;\n2- Человек;\n3 - Дворф\n4 - Другая\nВаша раса: ")
    if int(x) in range(1, 5):
        break
    else:
        print("Извини приятель, я не расслышал, так откуда ты?")
    first_guest = False

while True:
    if x == 1:
        print("Оо добро пожаловать! Специально для вас у нас есть...")
        break
    elif x == 2:
        print("Приветсвую сородич! А людей становится все меньше в этом городке, не находишь? Садись за стойку, расскажи о своих странствиях за кружкой бесплатного орчего пива!")
        break
    elif x == 3:
        print("Как раз сегодня привезли партию лучшего гномского эля, держи кружечку!")
        break
    else:
        print("Не узнаю я тебя... А мы не любим чужаков... правда парни? \n*Немногочисленные посетители кинули на вас недовольные взгляды, некоторые встали со своих мест и приготовили свое оружи.*\n-Сегодня вы выбрали не лучшее место чтобы умереть.")
        break














