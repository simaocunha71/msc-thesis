    def count_nums(arr):
        count = 0
        for num in arr:
            if num > 0:
                sum_digits = sum(int(digit) for digit in str(abs(num)))
                if sum_digits > 0:
                    count += 1
            elif num < 0:
                sum_digits = sum(int(digit) for digit in str(abs(num)) if digit != '0')
                if sum_digits > 0:
                    count += 1
        return count


