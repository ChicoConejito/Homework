my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0

while zero < len(my_list):
    number = my_list[zero]
    zero = zero + 1
    if number == 0:
        continue
    elif number < 0:
        break
    elif zero == len(my_list):
        print(number)
    else:
        print(number)
