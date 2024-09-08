
def large_product(a, b, k):
    result = []
    for i in a:
        for j in b:
            result.append(i*j)
    result.sort(reverse=True)
    return result[:k]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))

# Output: [60, 54, 50]

# Explanation:
# The products are [6*8, 6*9, 6*10, 8*9, 8*10, 9*10, 6*6, 2*8, 2*9, 2*10, 3*6, 3*8, 3*9, 3*10, 4*6, 4*8, 4*9, 4*10]
# Sorted in descending order, they become [90, 72, 60, 54, 50, 48, 36, 24, 20, 18, 18, 16, 15, 12, 12, 10, 10, 8].
# The three largest are [90, 72, 60].

"""
This function works by first creating a list of all possible products of the two input lists, then sorts that list in descending order, and finally returns the first k elements of the sorted list.
"""

# Note: This solution is inefficient for large inputs because it calculates every possible pair of products. A more efficient solution would use a heap or a different data structure to keep track of the k largest products.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
