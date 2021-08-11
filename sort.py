# случай с упорядоченным списком
list_of_numbers = [i for i in range(-100, 101, 20)] #генерируем список из 20 чисел от -100 до 100

def most_number(ls):
    last_three_numbers = ls[-1] * ls[-2] * ls[-3] #произведение последних трёх элементов списка
    first_two_numbers_and_last_number = ls[0] * ls[1] * ls[-1] #произведение первых двух элементов списка и последнего элемента списка
    if last_three_numbers > first_two_numbers_and_last_number:
        return last_three_numbers #480000
    elif last_three_numbers < first_two_numbers_and_last_number:
        return first_two_numbers_and_last_number #800000

if __name__ == "__main__":
    print("Упорядоченный список: ", list_of_numbers)
    print("Наибольшее произведение: ", most_number(list_of_numbers))