# Существует список чисел, представляющих собой дневные температуры 
# (в градусах Цельсия) в течение одного месяца (30 дней). 
# Ваша задача - реализовать несколько функций, которые выполняют следующие операции 
# с этим списком температур:


from random import randint 
from input_output import input_lst_temperature, output_temperature_lst


# Найти индекс первого дня, когда температура превысила заданное значение.
def search_index_day_gt(lst_temp):

    num = int(input("Введите заданное значение: "))

    for i in range(len(lst_temp)):
        if lst_temp[i] > num:
            return i 



def main():
    lst_temp = []

    input_lst_temperature(lst_temp)

    output_temperature_lst(lst_temp)

    print("Задание №1")
    index_gt = search_index_day_gt(lst_temp)
    print(f"Индекс первого дня, когда температура превысила заданное значение: {index_gt}")

main()