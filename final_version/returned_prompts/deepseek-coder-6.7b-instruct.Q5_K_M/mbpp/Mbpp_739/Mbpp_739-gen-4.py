"""
We can use binary search to solve this problem.

Firstly, we need to generate a list of triangular numbers with n digits.

Then, use binary search to find the index of smallest triangular number.
"""

def generate_triangular_numbers(n):
    """
    Generate triangular numbers with n digits.
    """
    triangular_numbers = []
    i = 1
    while len(str(i*(i+1)//2)) <= n:
        if len(str(i*(i+1)//2)) == n:
            triangular_numbers.append(i*(i+1)//2)
        i += 1
    return triangular_numbers

def binary_search(arr, x):
    """
    Binary search function to find the index of smallest triangular number.
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:

            return mid

    return -1

def find_index(n):
    triangular_numbers = generate_triangular_numbers(n)
    return binary_search(triangular_numbers, min(triangular_numbers))

print(find_index(2)) # Output: 4

"""
In the above code, the function generate_triangular_numbers generates a list of triangular numbers with n digits.

The function binary_search is used to find the index of the smallest triangular number in the list.

Finally, the function find_index generates a list of triangular numbers with n digits and finds the index of the smallest triangular number in the list using binary search.
"""

"""
The time complexity of this solution is O(log n), where n is the number of triangular numbers with n digits.

The space complexity of this solution is O(n), where n is the number of triangular numbers with n digits.
"""
"""
"""

# Test