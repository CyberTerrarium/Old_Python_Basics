"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
в остальных случаях: <d> дн <h> час <m> мин <s> сек
"""

user_int = int(input("Введите число: "))

second = 60
minute = 60
hour = second * minute
day = 24 * hour

if user_int >= minute:
    if user_int >= hour:
        if user_int >= day:
            print(f"{user_int // day} дн,", end = " ")
            user_int -= day * (user_int // day)
        print(f"{user_int // hour} час,", end = " ")
        user_int -= hour * (user_int // hour)
    print(f"{user_int // minute} мин,", end = " ")
    user_int -= minute * (user_int // minute)

print(f"{user_int % second} сек.")

