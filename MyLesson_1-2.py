import time

input("Добро пожаловать в нашу компанию по подбору идельной квартиры в нашем комплексе \"Традиционный Европейский Дом\"! \nНажмити любую клавишу для подтверждения и тогда мы сможем подобрать для Вас самый лучший варинт прекрасной квартиры! ")
while True:
    first_and_last_name = input("Ваше имя и фамилия, пожалуйста введите их здесь: ")
    if first_and_last_name.strip():
        break
    for name in "Кажется Вы забыли ввести Ваше имя, пожалуйста заполните данное поле!":
        print(name, end='', flush=True, )  # Печатаем символ без переноса строки
        time.sleep(0.01)
    print()

while True:
    number = input("Номер телефона для связи: ")
    if number.strip():
        break
    for num in "Кажется Вы забыли ввести Ваше номер телефона для связи, пожалуйста заполните данное поле!":
        print(num, end='', flush=True, )  # Печатаем символ без переноса строки
        time.sleep(0.01)
    print()

print("А теперь самое приятное, давайте выбирать Ваш будущий очаг тепла и уюта в этом мире с бешенным темпом и ритмом! ")
print("Указанные Вами данные выше верны? ")
otvet = input("Введите \"y\", если данные верны, если нет, то \"n\"")
if otvet == "y":
    print()
elif otvet == "n":
    for in_time_text_bukva in "Кажется произошла ошибка, попробуйте и...ль__вать __-":
        print(in_time_text_bukva, end='', flush=True,)  # Печатаем символ без переноса строки
        time.sleep(0.1)
    time.sleep(3)
    for in_time_text in f"\nОх хо-хох, а данные хорошии, да! ... ВЫ нам ОЧЕНЬ подходите, {first_and_last_name}":
        print(in_time_text, end='', flush=True,)  # Печатаем символ без переноса строки
        time.sleep(0.1)
floor_house = int(input(f"Прекрасно! Для начала нужно определиться, в здании с какой этажностью вы хотите жить? Это будет уютный представитель европейских домиков, этажность которого будет равно 4 или высотное здания, с прекрасным видом на весь город, которое устремляется ввысь на 30 этажей? Выбирать только вам! \nЭтажность будущего дома: "))
while floor_house != 4 and floor_house != 30:
    if floor_house == 4:
        print("Прекрасный выбор! здешний уют узких улочек и тень раскидистых крон деревьев создают неповторимо уютную атмосферу, а в жаркий летний день создадут прохладу! ")
        break
    if floor_house == 30:
        print("Замечательный выбор! В вашем распоряжении будет лучший вид на целый город! Просыпаться под нежное утреннее солнце и завтракать рассматривая целый город, что может быть лучше? А в придачу вы получаете и самый свежий воздух в городе, хе-хе, экономия на очистке воздуха как-никак!")
        break
    else:
        floor_house = int(input("Прошу прощения, но вы указали некорректные данные, попробуйте еще раз! \nКакая этажность Вашего будущего дома больше нравится: "))

floor = int(input("Желаемый этаж расположения вашей квартиры: "))
if 1 <= floor <= 4:
    print("Прекрасно!")