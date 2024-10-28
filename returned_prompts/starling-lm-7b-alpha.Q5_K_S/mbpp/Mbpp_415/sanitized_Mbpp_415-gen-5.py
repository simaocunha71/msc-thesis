def max_Product(A):
    maxProduct = (-float("inf"), -float("inf"))
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] * A[j] > maxProduct[0] * maxProduct[1]:
                maxProduct = (A[i], A[j])
    return maxProduct