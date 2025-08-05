def is_multiple(check_number, number):
    if check_number % number == 0:
        return True


for i in range(100, 0, -1):
    if is_multiple(i, 4):
        print(i)
