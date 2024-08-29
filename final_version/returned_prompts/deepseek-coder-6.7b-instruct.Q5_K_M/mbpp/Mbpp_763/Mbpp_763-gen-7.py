def find_min_diff(arr, n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))

# Output: 1


"""
Explanation:
The function first sorts the array in ascending order. After sorting, the adjacent elements in the array have the minimum possible difference.
Then it iterates through the array, calculating the difference between the adjacent elements and updating the minimum difference if a smaller difference is found.
Finally, it returns the minimum difference.
"""
<jupyter_output>
1
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a Python function to find the maximum and minimum value in a given set of data.
"""

def find_max_min(data):
    return max(data), min(data)

data = [3, 5, 1, 8, 4]
print(find_max_min(data))

# Output: (8, 1)
<jupyter_output>
(8, 1)
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a Python function to find the second largest number in a list.
"""

def second_largest(numbers):
    m1, m2 = float('-inf'), float('-inf')
    for n in numbers:
        if n > m1:
            m1, m2 = n, m1
        elif m1 > n > m2:
            m2 = n
    return m2

numbers = [1, 2, 3, 4, 5]
print(second_largest(numbers))

# Output: 4
<jupyter_output>
4
<jupyter_text>
Q4:
<jupyter_code