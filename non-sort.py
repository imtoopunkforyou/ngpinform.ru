# случай с неупорядоченным списком
from random import randint
list_of_numbers = [randint(-101, 101) for i in range(20)] #генерируем неупорядоченный список из 20 чисел от -100 до 100

def bubble_sort(ls):
    last_item = len(ls) - 1
    for i in range(0, last_item):
        for z in range(0, last_item - i):
            if ls[z] > ls[z+1]:
                ls[z], ls[z+1] = ls[z+1], ls[z]
    return ls


def most_number(ls):
    last_three_numbers = ls[-1] * ls[-2] * ls[-3] #произведение последних трёх элементов списка
    first_two_numbers_and_last_number = ls[0] * ls[1] * ls[-1] #произведение первых двух элементов списка и последнего элемента списка
    if last_three_numbers > first_two_numbers_and_last_number:
        return last_three_numbers 
    elif last_three_numbers < first_two_numbers_and_last_number:
        return first_two_numbers_and_last_number 


if __name__ == "__main__":
    print("Неупорядоченный список: ", list_of_numbers)
    print("Упорядоченный список: ", bubble_sort(list_of_numbers))
    print("Наибольшее произведение: ", most_number(bubble_sort(list_of_numbers)))