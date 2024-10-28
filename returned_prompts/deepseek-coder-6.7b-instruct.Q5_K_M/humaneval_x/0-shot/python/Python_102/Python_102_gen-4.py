
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i
    return -1

print(choose_num(12, 15))  # 14
print(choose_num(13, 12))  # -1


This solution starts from the upper limit (y) and keeps decreasing the value of the variable 'i' until it reaches the lower limit (x). For every number in this range, it checks if the number is even by using the modulo operation (i % 2 == 0). If the number is even, it returns the number immediately. If the function completes the loop without finding an even number, it returns -1.


This problem is very suitable for a loop-based solution as it involves a sequence of numbers and a condition to check for each number in the sequence. The solution also demonstrates the power of Python's range function to iterate in a specific direction.


This problem is also a good example of how to use the modulo operation to check for even numbers.
"""

# problem 2

"""
