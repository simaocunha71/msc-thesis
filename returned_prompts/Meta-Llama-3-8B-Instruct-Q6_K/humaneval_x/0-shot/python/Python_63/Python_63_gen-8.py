    def fibfib(n: int):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 0, 1
            for _ in range(3, n+1):
                a, b, c = b, c, a + b + c
            return c
    # Test cases
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
    # Time complexity: O(n)
    # Space complexity: O(1)  # Only 3 variables are used.  



# https://www.geeksforgeeks.org/program-to-find-nth-fibonacci-number-using-memoization/  # memoization
def fibfib(n: int):
    if n <= 1:
        return 0
    memo = {0: 0, 1: 0, 2: 1}  # Base cases
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]
# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
# Time complexity: O(n)
# Space complexity: O(n)  # The dictionary memo has n+1 entries.  



# https://www.geeksforgeeks.org/program-to-find-nth-fibonacci-number-using-bottom-up-dynamic-programming/  # bottom-up dynamic programming
def fibfib(n: int):
    if n <= 1:
        return 0
    fib = [0, 0, 1]  # Base cases
    for i in range(3, n+1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3])
    return fib[n]
# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
# Time complexity: O(n)
# Space complexity: O(n)  # The list fib has n+1 entries.  



#