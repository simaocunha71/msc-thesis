        if i in B:
            res.add(i)

    # Return the result set
    return res

# Driver code
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

# Function call
print(intersection(A, B))
# Output: {3, 4, 5}

"""
The time complexity of this algorithm is O(n) as it iterates over the length of the tuple and the space complexity is O(1) as it only uses a tuple of the same length of the input tuples.
"""



# Python3 program to find the
# intersection of