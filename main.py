#  Натуральные числа, содержащие хотя бы одну цифру, введенную с клавиатуры. Данную цифру выводить прописью.

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
slovar = {

    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}


def num_to_text(number):
    return slovar[number]


# -----------------------Введение проверочных цифр-----------------------

control_line = str(input('Введите цифры: '))
control_num = []
print('Введённые цифры: ')
for i in range(len(control_line)):
    if control_line[i] in num_list:
        control_num.append(control_line[i])
        print(num_to_text(control_line[i]))

print('-------')

# -----------------------Введение проверяемых чисел---------------------

with open('data_list.txt', 'r') as f:

    temp = ''
    work = True
    i = 0
    upcoming_num = []
    answer = ''

# ----------------------Разделение блоков информации---------------------

    while work:
        temp = ''
        data_byte = f.read(1)
        
        if data_byte == '\n':
            data_byte = ' '

        if data_byte != ' ' or len(data_byte) == 0:
            upcoming_num.append(data_byte)

# -----------------------Проверка блока на условие-----------------------

        elif data_byte == ' ':
            try:
                for i in upcoming_num:
                    temp += i
                temp = int(temp)


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
            except ValueError:
                upcoming_num = []

        if data_byte == '':
            try:
                for i in upcoming_num:
                    temp += i
                temp = int(temp)
                temp = ''

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
            except ValueError:
                upcoming_num = []

            work = False

        check = False



