number = abs(int(input("Введите целое число: ")))

digits_sum = 0
odd_digits_sum = 0
max_digit = 0

while number > 0:
    digit = number % 10
    digits_sum += digit

    if digit % 2 != 0:
        odd_digits_sum += digit

    if digit > max_digit:
        max_digit = digit

    number //= 10

print(f"Сумма цифр числа = {digits_sum}")
print(f"Сумма нечетных цифр числа = {odd_digits_sum}")
print(f"Максимальная цифра числа = {max_digit}")
