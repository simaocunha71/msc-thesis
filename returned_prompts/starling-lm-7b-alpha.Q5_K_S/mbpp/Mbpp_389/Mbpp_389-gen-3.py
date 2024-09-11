def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)


find_lucas(9)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


# Python3 program to print nth Lucas
# number using recursion.

# Returns nth Lucas number
def lucas(n, m):
    # Base Cases
    if n == 0:
        return 2
    if n == 1:
        return 1

    # Recurrence relation
    return (lucas(n - 1, m) + lucas(n - 2, m)) % m

# Driver Program
n = 9
m = 1000000007
print(lucas(n, m))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Python3 program to print nth Lucas
# number using bottom-up approach.

# Returns nth Lucas number using bottom-up approach
def lucas(n):
    # Base Case
    if n == 0:
        return 2
    if n == 1:
        return 1

    # Create an array to store results
    # of all subproblems
    luc = [0]*(n+1)
    luc[0] = 2
    luc[1] = 1

    # Initialize result for values
    # one step ahead
    for i in range(2, n+1):
        luc[i] = (luc[i-1] + luc[i-2]) % 1000000007

    return luc[n]

# Driver Code
n = 9
print(lucas(n))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Python3 program to print nth Lucas
# number using top-down approach.
