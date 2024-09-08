def sum_negativenum(lst):
    sum = 0
    for i in lst:
        if i < 0:
            sum += i
    return sum

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))  # Output: -32

"""
The function `sum_negativenum` takes a list of numbers as input, initializes a variable `sum` to 0, then iterates over each number `i` in the list. If `i` is a negative number, it adds `i` to `sum`. Finally, it returns the total sum.
"""

"""
This code is written in Python. It iterates over the list of numbers, checks if the number is negative, and if it is, it adds it to the sum. The sum of the negative numbers is then returned.
"""
<jupyter_output>
-32
<jupyter_text>
Q2. Write a Python function to find the maximum and minimum numbers from a given list of numbers.
<jupyter_code>
def find_max_min(lst):
    max_num = max(lst)
    min_num = min(lst)
    return max_num, min_num

# Example usage:
numbers = [5, 1, 9, 3, 7]
max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
<jupyter_output>
Maximum number: 9
Minimum number: 1
<jupyter_text>
Q3. Write a Python function to find the average of a list of numbers.
<jupyter_code>
def find_average(lst):
    return sum(lst) / len(lst)

# Example usage:
numbers = [5, 1, 9, 3, 7]
average = find_average(numbers)
print("Average:", average)
<jupyter