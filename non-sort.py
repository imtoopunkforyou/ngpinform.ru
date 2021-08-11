# случай с неупорядоченным списком
from random import randint
list_of_numbers = [randint(-100, 101) for i in range(1000)] #генерируем неупорядоченный список из 1000 чисел от -100 до 100

# def most_number(ls):
#     last_three_numbers = ls[-1] * ls[-2] * ls[-3] #произведение последних трёх элементов списка
#     first_two_numbers_and_last_number = list_of_numbers[0] * list_of_numbers[1] * list_of_numbers[-1] #произведение первых двух элементов списка и последнего элемента списка
#     if last_three_numbers > first_two_numbers_and_last_number:
#         return last_three_numbers #970200
#     elif last_three_numbers < first_two_numbers_and_last_number:
#         return first_two_numbers_and_last_number #990000

# print(most_number(list_of_numbers))

print(list_of_numbers)