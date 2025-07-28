start_number = int(input("Введите начальное число диапазона: "))
end_number = int(input("Введите конечное число диапазона: "))

numbers_sum = 0
numbers_count = 0

even_numbers_sum = 0
even_numbers_count = 0

if start_number < end_number:
    while start_number <= end_number:
        numbers_sum += start_number
        numbers_count += 1

        if start_number % 2 == 0:
            even_numbers_sum += start_number
            even_numbers_count += 1

        start_number += 1

    even_numbers_average = even_numbers_sum / even_numbers_count
    print(f"Среднее арифметическое чётных чисел = {even_numbers_average}")

    numbers_average = numbers_sum / numbers_count
    print(f"Среднее арифметическое чисел = {numbers_average}")
else:
    print("Начальное число должно быть меньше, чем конечное число. Попробуйте ввести ещё раз.")
