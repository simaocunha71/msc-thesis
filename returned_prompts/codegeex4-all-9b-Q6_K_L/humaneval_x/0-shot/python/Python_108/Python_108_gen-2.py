def count_nums(arr):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    return len([x for x in arr if sum_digits(x) > 0])

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)