# Существует список чисел, представляющих собой дневные температуры 
# (в градусах Цельсия) в течение одного месяца (30 дней). 
# Ваша задача - реализовать несколько функций, которые выполняют следующие операции 
# с этим списком температур:

from random import randint 
from input_output import input_lst_temperature, output_temperature_lst
from search_day_temp import search_index_day_gt, search_index_day_lt





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

main()