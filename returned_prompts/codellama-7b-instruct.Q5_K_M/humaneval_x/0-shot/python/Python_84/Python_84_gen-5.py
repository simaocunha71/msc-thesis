
def solve(N):
    # Write your code here
    result = 0
    while N > 0:
        result += N % 2
        N //= 2
    return bin(result)[2:]