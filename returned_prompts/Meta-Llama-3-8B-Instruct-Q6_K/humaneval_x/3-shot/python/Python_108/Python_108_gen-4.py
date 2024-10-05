    def count_nums(arr):
        return sum(1 for num in arr if sum(int(digit) for digit in str(abs(num))) > 0)  # count the number of elements in the array that have a sum of digits > 0


