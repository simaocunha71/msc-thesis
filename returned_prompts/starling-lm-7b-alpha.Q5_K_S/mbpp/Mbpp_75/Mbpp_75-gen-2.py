"""
def find_tuples(tuples, k):
    res = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            res.append(t)
    return res
"""

def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
# Output: [(6, 24, 12)]


"""
Explanation:
The function `find_tuples` takes two arguments: `tuples` which is the list of tuples, and `k` which is the divisor.
Inside the function, a variable `res` is initialized as an empty list to store the result.
Then, a list comprehension is used to iterate over each tuple `t` in the `tuples` list.
The `all` function is used to check if all the elements in the tuple are divisible by `k`. If so, the tuple is appended to the result list `res`.
Finally, the result list `res` is returned.
The given test case `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` is passed, which means that the function correctly finds the tuple `(6, 24, 12)` that has all elements divisible by 6 from the given list of tuples.
"""

"""
Time Complexity: O(n*m)
Space Complexity: O(n)
"""


"""
Alternative Solution:
"""

def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

# Test
print(find_tuples([(6, 2