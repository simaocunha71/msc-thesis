    def sum_of_digits(x):
        return sum(map(int, str(abs(x))))

    def count_nums(arr):
        return sum(map(sum_of_digits, arr)) > 0


