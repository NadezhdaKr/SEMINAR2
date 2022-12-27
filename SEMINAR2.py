# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

n = int(input('Введите число '))
fac_list = [0] * n

for i in range(n):
    fac_list[i] = factorial(i + 1)
print(fac_list)


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

x = [0, 1]
y = [0, 1]
print("x| y| ¬ X ∨ Y")
for x in range(0 , 2):
    for y in range(0, 2):
        sum = not x or y
        print(f"{x}| {y}| {int (sum)}")


 # Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

def count_the_symbols(string1, string2):
    for i in range(len(string1)):
        print(f"{string1[i]} - {string2.count(string1[i])}")
        
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
count_the_symbols(string1, string2)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.


def create_list(number):
    new_list = []
    for i in range(-number, number + 1):
        new_list.append(i)

    return new_list


def hyper_push_list(some_list, number_of_push):
    push_number = number_of_push
    new_list = []
    for i in range(-push_number, len(some_list) - push_number):
        new_list.append(some_list[i])

    return new_list


user_number = int(input('Введите число: '))
user_push = int(input('Введите размер сдвига: '))
my_list = create_list(user_number)

print(f'Начальный список -> {my_list} <-')
print(f'Новый список -> {hyper_push_list(my_list, user_push)} <- сдвинутый на {user_push} элемент \
                                                                                    {"ов" if user_push > 4 else "а"}')