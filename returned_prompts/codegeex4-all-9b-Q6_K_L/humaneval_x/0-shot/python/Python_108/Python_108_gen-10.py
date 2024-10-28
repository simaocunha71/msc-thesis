def count_nums(arr):
    def sum_digits(n):
        total = 0
        for i in str(n):
            total += int(i)
        return total
    return sum(1 for i in arr if sum_digits(i) > 0)

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)