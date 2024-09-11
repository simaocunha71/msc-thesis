"""
def sort_counter(dictionary):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
"""

def sort_counter(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1])


# assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]


# Python3 program to print all permutations of string
# This program prints all permutations of the string

# Function to print all permutations of string
def permute(a, l, r):
    # Base Case
    if l == r:
        print("".join(a))
    else:
        # Fix the element at the leftmost position
        for i in range(l, r + 1):
            # Swap the fixed element with the element at the rightmost position
            a[l], a[i] = a[i], a[l]
            # Recursively call for the case when the left index is incremented by 1
            permute(a, l + 1, r)
            # Backtrack
            a[l], a[i] = a[i], a[l]
# Driver program to test above function


a = [1, 2, 3]
n = len(a)
permute(a, 0, n - 1)

# This code is contributed by PrinciRaj11







































































































































