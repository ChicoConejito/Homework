numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num = 0
primes = []
not_primes = []
i = 0

for i in range(len(numbers)):
    is_prime = True
    num = numbers[i]
    if num < 2:
        print(num, 'Не простое и не сложное число')
        continue
    else:
        f = num ** (1 / 2)
        for j in range(2, int(f + 1)):
            if num % j == 0:
                is_prime = False
                break
        if not (is_prime):
            not_primes.append(num)
        else:
            primes.append(num)
    is_prime = True

print('Простые числа ', primes)
print('Составные числа', not_primes)