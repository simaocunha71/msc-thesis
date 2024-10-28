

def string_sequence(n: int) -> str:
    return " ".join(str(i) for i in range(n+1))


print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'


# Another approach

def string_sequence(n: int) -> str:
    result = ""
    for i in range(n+1):
        result += str(i) + " "
    return result.rstrip()  # remove the trailing whitespace


print(string_sequence(0))  # '0'
print(string_sequence(5))  # '0 1 2 3 4 5'

"""
Time complexity: O(n)
Space complexity: O(n)
"""

"""
Explanation:
1. We are using the range function to generate a sequence of numbers from 0 to n inclusive.
2. We are using the join function to convert the sequence into a string, where each number is separated by a space.
3. In the first approach, we are using a generator expression to generate the sequence of numbers.
4. In the second approach, we are using a for loop to generate the sequence of numbers and concatenate them to the result string.
"""

# The following approach is using recursion
def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    else:
        return string_sequence(n - 1) + ' ' + str(n)

print(string_sequence(5))  # '0 1 2 3 4 5'

"""
Time complexity: O(n)
Space complexity: O(n)
"""

"""
Explanation:
1. We are using the recursive function string_sequence to generate the sequence of numbers.
2. The base case is when n is 0, we return '0'.
3. For other values of n, we recursively call string_sequence with n - 1 and append n to the result. We also append a space to separate the numbers.
"""
<jupyter_output>
0