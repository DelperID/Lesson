# ПЕРЕМЕННЫЕ и взаимодействие с ними

mobile, name = ("+77058110592"), ("Dmitry")
print(mobile, name)
Tphone = mobile
print(Tphone)
 
print()

number1 = 13
number2 = 10
number3 = 8
result = number1 + number2
print(result)

print()

number1, number2 = number2, number1 + number3 + 4
print(number1, number2)

print()

number2 -= number3
print(number2, number1, number3, sep="\n")

print()

z, x, c, *other = ["Значение переменной 1", 2, 3, 4, 5, number2] # В # данном случае список слишком длинный и
# по этому чтобы распаковать все значения, нужно добавить переменную с символом "*" чтобы через
#  нее вывести все значения, превышающие количество переменных
print(z)
print(x)
print(c)
print(other)

