# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
#
# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1         2         3         4         5          6
# 2         4         6         8         10         12
# 3         6         9         12        15         18
# 4         8        12         16        20         24
# 5        10        15         20        25         30
# 6        12        18         24        30         36

# def print_operation_table(operation, num_rows = 6, num_columns = 6):
#     space = ' '
#     list_1 = [1, 2, 3, 4, 5, 6]
#     list_2 = [1, 2, 3, 4, 5, 6]
#
#     print(list_1)
#     for i, j in enumerate(list_1, 1):
#
#         for k, l in enumerate(list_2, 1):
#                                          # for j in range(len(list_2)):
#             mult = i * k
#             print(f'{space} {mult}  ')
# print_operation_table(lambda x, y: x * y)
def print_operation_table(operation, num_rows = 6, num_columns = 6 - 1):
    i = 1

    j = 0
    while  j <= num_columns :
        num_rows * j
        i = 1
        j += 1
        print()
        while i <= num_rows:
            print(i * j, end="   ")
            i += 1



print_operation_table(lambda x, y: x * y)