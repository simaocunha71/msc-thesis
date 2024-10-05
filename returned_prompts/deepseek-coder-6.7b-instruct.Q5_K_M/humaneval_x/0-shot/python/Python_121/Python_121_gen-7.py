
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0)

Test cases:

print(solution([5, 8, 7, 1])) # 12
print(solution([3, 3, 3, 3, 3])) # 9
print(solution([30, 13, 24, 321])) # 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 3
print(solution([2, 2, 2, 2, 2, 2, 2, 2, 1])) # 1

"""
Explanation:

In the first example, the odd numbers in even positions are 5 and 7, so the sum is 12.
In the second example, all numbers are odd, so the sum is 9.
In the third example, there are no odd numbers in even positions, so the sum is 0.
In the fourth example, the odd numbers in even positions are 1 and 5, so the sum is 3.
In the fifth example, the odd numbers in even positions are 2 and 1, so the sum is 1.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python program to find the maximum and minimum numbers from the given list.
<jupyter_code>
