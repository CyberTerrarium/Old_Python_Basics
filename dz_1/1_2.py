"""
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
 Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""

numbers_list = [number**3 for number in range(1, 1001, 2)]
result_sum_1, result_sum_2 = 0, 0

for number in numbers_list:
    avg_sum_1, avg_sum_2 = 0, 0
    temp_number_1, temp_number_2 = number, number + 17

    while temp_number_1:
        avg_sum_1 += temp_number_1 % 10
        temp_number_1 //= 10

    while temp_number_2:
        avg_sum_2 += temp_number_2 % 10
        temp_number_2 //= 10

    if (avg_sum_1 % 7 == 0):
        result_sum_1 += number

    if (avg_sum_2 % 7 == 0):
        result_sum_2 += number + 17

print(result_sum_1)
print(result_sum_2)