# ngpinform-ru
task for www.ngpinform.ru

Задача:
У вас есть массив с целыми числами, в том числе и отрицательными, вам нужно найти самое большое произведение 3 чисел из этого массива. Задание нужно выполнить максимально эффективно, не забывая про отрицательные числа.
Например: у вас есть массив list_of_ints, содержащий числа -10, -10, 1, 3, 2. Функция, которая обрабатывает этот массив, должна вернуть 300, так как -10 * -10 * 3 = 300.

Решение:
Так как в задании не указано, с каким видом списка предстоит работать - упорядоченным или нет - решение имеет два пути. Файл non-sort.py реализует решение для неупорядоченного списка, в то время как sort.py реализует упорядоченный список.

Алгоритм действий:
1. Сортируем список, если он не был отсортирован
    1.1 Для сортировки был использован алгоритм "Сортировка пузырьком". Выбор на него пал не потому что он самый оптимальный, а потому что я его помню со времен учебы в университете. Стандартная сортировка массива способом list.sort([key=функция]) работает быстрее и имела бы место быть в реальном проекте, но не в случае проверки кандитата на вакансию.
2. В упорядоченном списке находим произведение первых двух чисел и последнего числа.
    2.1 Для умножения элементов списка так же можно использовать numpy.prod(list)
3. В упорядоченном списке находим произведение последних трёх чисел списка.
    3.1 Для умножения элементов списка так же можно использовать numpy.prod(list)
4. Сравниваем числа, выводим наибольшее из них 
