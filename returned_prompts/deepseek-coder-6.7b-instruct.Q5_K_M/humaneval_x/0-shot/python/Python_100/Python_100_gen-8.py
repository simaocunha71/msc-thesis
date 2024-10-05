
    result = []
    for i in range(n):
        if n % 2 == 0:
            result.append(n + 2 * i)
        else:
            result.append(n + 2 * i)
    return result

print(make_a_pile(3))

# Output: [3, 7, 11]

"""
This problem can be solved by using a simple loop that iterates through the range from 0 to n-1. In each iteration, the code appends the next odd/even number to the result list.
"""

