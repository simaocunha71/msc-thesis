def count_nums(arr):
    def sum_digits(num):
        s = 0
        for digit in str(abs(num)):
            s += int(digit)
        return s

    return len([x for x in arr if sum_digits(x) > 0])

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)