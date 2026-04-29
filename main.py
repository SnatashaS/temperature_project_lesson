# Существует список чисел, представляющих собой дневные температуры 
# (в градусах Цельсия) в течение одного месяца (30 дней). 
# Ваша задача - реализовать несколько функций, которые выполняют следующие операции 
# с этим списком температур:
#https://github.com/MaximBytecamp/temperature_projects - ссылка на проект

from random import randint 
from input_output import input_lst_temperature, output_temperature_lst
from search_day_temp import search_index_day_gt, search_index_day_lt

# Подсчитать количество дней, когда температура была ниже заданного значения.
def count_day_temperature(lst_temp):
    num = int(input("Введите заданное значение: "))

    count_day = 0 

    for el in lst_temp: 
        if el <= num: 
            count_day += 1 

    return count_day

# Добавить в список температур еще один список температур за последние несколько дней месяца.
def append_new_temp(lst_temp):
    lst_temp_copy = lst_temp.copy()

    count_temp = int(input("Сколько новых температур будем добавлять? -> "))

    if count_temp is None or count_temp <= 0:
        print("Значение пустое или меньше-равно нуля")
        return 
    
    for i in range(count_temp):
        lst_temp_copy.append(int(input(f"Введите {i+1}. температуру: ")))

    return lst_temp_copy 
        



def main():
    lst_temp = []

    input_lst_temperature(lst_temp)

    output_temperature_lst(lst_temp)

    print("Задание №1")
    index_gt = search_index_day_gt(lst_temp)
    print(f"Индекс первого дня, когда температура превысила заданное значение: {index_gt}")


    print("Задание №2")
    index_lt = search_index_day_lt(lst_temp)
    print(f"Индекс первого дня, когда температура превысила заданное значение: {index_lt}")
    

    print("Задание №3")
    count_day = count_day_temperature(lst_temp)
    print(f"Подсчитать количество дней, когда температура была ниже заданного значения.: {count_day}")


    print("Задание №4")
    lst_temp_copy = append_new_temp(lst_temp)
    print(f"Добавить в список температур еще один список температур за последние несколько дней месяца.")
    output_temperature_lst(lst_temp_copy)
    print("Исходный список для сравнения:")
    output_temperature_lst(lst_temp)

main()