list_of_ints = [-100, -99, -50, -30,-10, -10, 1, 2, 3, 5, 10, 15, 20, 30, 40, 50, 70, 80, 100]
list_of_last_three_numbers = []
list_of_first_two_numbers_and_last_number = []

list_of_last_three_numbers.append(list_of_ints[-3:])
list_of_first_two_numbers_and_last_number.append(list_of_ints[-1:])
list_of_first_two_numbers_and_last_number.append(list_of_ints[0:2])
print(list_of_ints)
print(list_of_last_three_numbers)
print(list_of_first_two_numbers_and_last_number)
