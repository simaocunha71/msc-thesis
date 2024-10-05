
    def count_nums(arr):
        count = 0
        for num in arr:
            sum_digits = sum(int(digit) for digit in str(abs(num)))
            if num < 0 and sum_digits % 2 == 0:
                count += 1
            elif num >= 0 and sum_digits % 2 != 0:
                count += 1
        return count

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)

