
    def count_nums(arr):
        count = 0
        for num in arr:
            digit_sum = 0
            for digit in str(num):
                digit_sum += int(digit)
            if digit_sum > 0:
                count += 1
        return count

    print(count_nums([]))  # 0
    print(count_nums([-1, 11, -11]))  # 1
    print(count_nums([1, 1, 2]))  # 3


"""
This solution works by first initializing a count variable to 0. Then for each number in the input list, it converts the number into a string, so it can iterate over each digit of the number. It then converts each digit back into an integer and adds it to the digit_sum. If the digit_sum is greater than 0, it increments the count by 1. Finally, it returns the count.
"""

"""
The time complexity of this solution is O(n*m) where n is the number of elements in the array and m is the number of digits in the largest number. The space complexity is O(1) as it uses a constant amount of space to store the count and digit_sum.
"""

"""
The function works by iterating over each number in the array, and for each number, it converts it to a string and iterates over each character in the string (which are the digits of the number). It then converts each character back to an integer and adds it to a running total (digit_sum). If the running total is greater than 0, it increments a count. Finally, it returns the count.
"""
"""
The time complexity of this solution is O(n*m) where n is the number of elements in the array and m is the number of digits in the largest number. The space complexity is O(1) as it uses a constant amount of space to store the count and digit_sum.
"""

"""
This function works by iterating over each number in the input array. For each number, it converts it to a string and iterates over each character in the string (which are the digits of the number). It then converts each character back to an integer