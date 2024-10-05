    def count_nums(arr):
        count = 0
        for num in arr:
            if num >= 0:
                if sum(int(digit) for digit in str(num)) > 0:
                    count += 1
            else:
                if sum(int(digit) if digit != '-' else 0 for digit in str(num)) > 0:
                    count += 1
        return count


