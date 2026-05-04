from input_output import input_lst_temperature, output_temperature_lst

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
        


#Удалить температуру последних дней из списка.
def del_temp_lst(lst_temp):
    
    lst_temp_copy = lst_temp.copy()

    day = int(input("Сколько последних температур из списка будем удалять -> "))
    #[1,2,3,4,5] -> day = 3 -> range(3) -> 0 1 2 -> del lst[-1] -> 5 -> [1,2,3,4] -> del lst[-1] -> 4 -> [1,2,3] -> lst[-1] -> 3 -> [1,2]
    for _ in range(day): 
        del lst_temp_copy[-1]

    return lst_temp_copy 


# Объединить два списка температур, представляющих собой данные двух разных месяцев.
def extend_union_lst():
    lst_temp1 = input_lst_temperature()
    output_temperature_lst(lst_temp1)
    lst_temp2 = input_lst_temperature()
    output_temperature_lst(lst_temp2)

    lst_temp1.extend(lst_temp2) #[1,2,3,4].extend([2,3,5]) -> [1,2,3,4,2,3,5]  
    return lst_temp1

    #append -> in place -> res = lst.append(5) -> print(res)