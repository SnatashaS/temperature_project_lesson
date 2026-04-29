# Найти индекс первого дня, когда температура превысила заданное значение.
def search_index_day_gt(lst_temp):

    num = int(input("Введите заданное значение: "))

    for i in range(len(lst_temp)): #lst_temp = [10,20,30] -> range(len(lst_temp)) -> [0,1,2]
        if lst_temp[i] > num:
            return i 

# Найти индекс последнего дня, когда температура не превышала заданное значение.
def search_index_day_lt(lst_temp):

    num = int(input("Введите заданное значение: "))

    for i in range(len(lst_temp)-1,0-1,-1):
        if lst_temp[i] < num:
            return i 