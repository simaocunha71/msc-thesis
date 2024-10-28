def count_nums(arr):
    def count_digits(n):
        """
        This function takes an integer n and returns the number of digits in it.
        """
        return len(str(abs(n)))

    def sum_digits(n):
        """
        This function takes an integer n and returns the sum of its digits.
        """
        return sum(int(digit) for digit in str(abs(n)))

    return len([n for n in arr if sum_digits(n) > 0])

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)

This solution uses two helper functions, count_digits and sum_digits, to count the number of digits and the sum of digits in each integer in the array. The main function count_nums then returns the number of integers in the array that have a sum of digits greater than 0. The solution also includes unit tests to verify the correctness of the solution.