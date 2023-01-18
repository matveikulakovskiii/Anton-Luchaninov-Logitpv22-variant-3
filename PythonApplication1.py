
#3 Вариант


#1 
#// for  используеться используется для перебора последовательности элементов, например списка // Функция range() возвращает неизменяемую последовательность чисел между заданным начальным целым числом и конечным целым числом.// 
# Оборачивая input() функцией int(), мы преобразуем введеную строку в целое число.
n = int(input("Enter a number between 1 and 9: "))

for i in range(n):
    print(" ----- ")
    print("|  O  |")
    print("!  -  !")
    print(" ----- ")
#2 // break-делает завершение цикла2
power = int(input("Enter power: "))
n = int(input("Insert the number n: "))

for i in range(1, n+1):
    result = i ** power
    if result > n ** 3:
        break
    print(i, "^", power, "=", result)
#3 // len-возвращает количество символов в строке// sum - для получения суммы чисел итерации.
import random

grades = [random.randint(1, 5) for _ in range(10)]
average = sum(grades) / len(grades)

print("Grades:", grades)
print("Average grade:", average)

#4 // while-этот цикл позволяет программе перебирать блок кода.
gift = 1
years_passed = 0

while gift < 100:
    years_passed += 1
    gift += years_passed
    print("Year:", years_passed, "Gift:", gift)

print("It will take", years_passed, "years to reach 100$ gift.")
#5
n = int(input("Enter the number of Fibonacci numbers to generate: "))

a = 0
b = 1

print(a)
print(b)

for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c
