# Подсчитать количество дней, когда температура была ниже заданного значения.
def count_day_temperature(lst_temp):
    num = int(input("Введите заданное значение: "))

    count_day = 0 

    for el in lst_temp: 
        if el <= num: 
            count_day += 1 

    return count_day


#lst=[1,2,3,4] 
#lst.append([2,3]) -> [1,2,3,4,[2,3]]
#lst.extend([2,3]) -> [1,2,3,4,2,3]


# преобразовать список температур из Цельсия в Фаренгейты.
# Для пересчета по шкале Фаренгейта необходимо исходное значение температуры умножить на 1,8 и к результату прибавить 32

def selsia_in_farangeit(lst_temp):
    lst_temp_copy = lst_temp.copy()

    for i in range(len(lst_temp)):
        lst_temp_copy[i] = round((lst_temp_copy[i] * 1.8) + 32, 3)

    # return lst_temp_copy

    #[1,2,3,4]
    #[1,2,3,4] -> range(len([10,20,30,40])) -> [0,1,2,3]

    #lst_temp_copy[0] = (1 * 1.8) + 32 -> [34.5, 2, 3, 4]

    #lst_temp_copy[1] = (2 * 1.8) + 32 -> [34.5, 54.4, 3, 4 ]

    #...

    #lst_temp_copy[3] = (4 * 1.8) + 32 -> [34.5, 12.34, 213.423, 21421.4214]

    lst_result = []
    for el in lst_temp_copy:
        lst_result.append(round(el * 1.8 + 32, 3)) #

    #lst_result = [], lst_temp_copy = [10,20,30,40]
    #el = 1 
    #1 * 1.8 + 32 -> lst_result.append(35) -> lst_result -> [35], lst_temp_copy -> [1,2,3,4]
    #el = 2 