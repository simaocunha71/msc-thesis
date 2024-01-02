
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    if not (1 <= N <= 10000):  # 1 <= N <= 10^4
        print("No solution!")
        return None
    
    total_sum = 0
    for i in range(len(str(N)) - 1, -1, -1):   # -1 is last index of string
        if (i % 2) == 0:  # print("even")
            total_sum += N // 2 * bin(int(N / 2), 2)[2:]
            
        else:   # print("odd")
            total_sum += N // 2 * bin(int((N - 1) / 2), 2)[2:]
    return str(total_sum)

if __name__ == '__main__':
    '''
        测试用例
        input:
            1000, 879456, 150
        output:
            "1", "110", "1100"
    '''