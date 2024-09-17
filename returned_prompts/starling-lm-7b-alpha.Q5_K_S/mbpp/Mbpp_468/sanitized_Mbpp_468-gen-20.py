def max_product(nums):
    stack = []
    for n in nums:
        if not stack or stack[-1] <= n:
            stack.append(n)
        else:
            stack.append(n * stack.pop())
    return stack[-1]