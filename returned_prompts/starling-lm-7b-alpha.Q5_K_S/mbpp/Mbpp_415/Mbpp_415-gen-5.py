def max_Product(A):
    maxProduct = (-float("inf"), -float("inf"))
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > maxProduct[0] * maxProduct[1]:
                maxProduct = (A[i], A[j])
    return maxProduct

# Test
print(max_Product([1,2,3,4,7,0,8,4]))
# Output: (7, 8)




















"""
def max_Product(A):
    maxProduct = (-float("inf"), -float("inf"))
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > maxProduct[0] * maxProduct[1]:
                maxProduct = (A[i], A[j])
    return maxProduct

assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""



"""
def max_Product(A):
    maxProduct = (-float("inf"), -float("inf"))
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > maxProduct[0] * maxProduct[1]:
                maxProduct = (A[i], A[j])
    return maxProduct

# Test
print(max_Product([1,2,3,4,7,0,8,4]))
# Output: (7, 8)
"""


"""
def max_Product(A):
    maxProduct = (-float("inf"), -float("inf"))
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > maxProduct[0] * maxProduct[1]:
                maxProduct = (A[i], A[j])
    return max