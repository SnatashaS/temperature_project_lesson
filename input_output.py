from random import randint

def input_lst_temperature(lst_temp):

    month = int(input("Введите текущий номер месяца (1-12) -> "))
    year = int(input("Введите текущий год: "))

    if not 1970 <= year <= 2026:
        return 

    if not 1 <= month <= 12:
        print(f"Извините, но такого месяца с номером {month} в природе нет!")
        return
    
    if month in [1,3,5,7,8,10,12]:
        for _ in range(31):
            lst_temp.append(randint(-10,30))

    elif month in [4,6,9,11]:
        for _ in range(30):
            lst_temp.append(randint(-20,20))

    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            for _ in range(29):
                lst_temp.append(randint(-30,0))
        else:
            for _ in range(28):
                lst_temp.append(randint(-30,0))

    
def output_temperature_lst(lst_temp):
    print(f"В вашем списке находится {len(lst_temp)} значений температур")

    print("ВАШ СПИСОК ТЕМПЕРАТУР: ")
    print("="*40)
    for el in lst_temp:
        print(el, end=", ")
    print()
    print("="*40)