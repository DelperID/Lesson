# while True:
#     x = int(input("Введите число: "))
#     count = 0
#     y = 1
#
#     while count < x:
#         count += 1
#         y *= count
#
#     else:
#         print(y)

x = ''

while len(x) < 5:
    y = input("Введите данные: ")
    if y == "o":
        continue
    if y == "l":
        break

    x += y

else:
    print(x)

print("Программа работает дальше")