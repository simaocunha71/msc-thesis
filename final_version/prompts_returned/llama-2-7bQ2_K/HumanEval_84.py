
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
    if (not isinstance(N, int)):
        return str(str(N).zfill(32))[:-1]

    count = 0 # keep track of the total sum of digits in binary
    
    while N > 0:
        digit_count = bin(int(N % 2)).count('1')
        
        if (digit_count == 0): # handle exception
            print("Error")
            return None
                             
        count += digit_count
        N //= 2
    return str(str(count).zfill(32))[:-1]  

N = int(input())
print(solve(int(N)))
