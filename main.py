from slovar import num_to_text

# -----------------------Введение проверочных цифр-----------------------

control_line = str(input('Введите цифры: '))
control_num = []
print('Введённые цифры: ')
for i in range(len(control_line)):
    if control_line[i] != ' ':
        control_num.append(control_line[i])
        print(num_to_text(control_line[i]))

print('-------')

# -----------------------Введение проверяемых чисел---------------------

with open('data_list.txt', 'r') as f:
    data_list = f.readline()

    i = 0
    upcoming_num = []
    answer = ''

# ----------------------Разделение блоков информации---------------------

    while True:
        try:  # try-exсept проверяет закончились ли поступающие блоки
            if data_list[i] != ' ':
                upcoming_num.append(data_list[i])

# -----------------------Проверка блока на условие-----------------------

            else:
                for num in control_num:
                    if num in upcoming_num:
                        check = True

# -------------------Замена на пропись подходящих цифр-------------------

                        for j in range(len(upcoming_num)):
                            if upcoming_num[j] == num:
                                upcoming_num[j] = num_to_text(num)
                if check:
                    for j in upcoming_num:
                        answer += j
                    print(answer)  # Вывод преобразованных чисел
                    answer = ''
                upcoming_num = []
            i += 1
            check = False

        except IndexError:  # Если блоки закончились, выводит последний блок
            for num in control_num:
                if num in upcoming_num:
                    check = True
                    for j in range(len(upcoming_num)):
                        if upcoming_num[j] == num:
                            upcoming_num[j] = num_to_text(num)
                if check:
                    for j in upcoming_num:
                        answer += j
                    print(answer)
            break
