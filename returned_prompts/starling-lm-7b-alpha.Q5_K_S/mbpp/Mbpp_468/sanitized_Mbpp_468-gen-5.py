def max_product(A):
    n = len(A)
    cur = 0
    max_product = 0
    stack = [0] * n
    for i in range(n):
        if stack[cur] < A[i]:
            stack[cur + 1] = A[i]
            cur += 1
        else:
            while cur >= 0 and stack[cur] >= A[i]:
                cur -= 1
            stack[cur + 1] = A[i]
            cur += 1
        if cur > max_product:
            max_product = cur
    return stack[max_product]