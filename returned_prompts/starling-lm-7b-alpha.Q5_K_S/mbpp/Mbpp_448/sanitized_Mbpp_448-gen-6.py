def cal_sum(n):
    # Perrin numbers are the numbers that appear in the expansion of (1+x)^n for n>=0
    # and are of the form C(n,k) where C(n,k) is the binomial coefficient of (n,k)
    # Summing all the numbers up to n, we get (2^n) - 1
    # So the sum of the perrin numbers up to n is (2^n)-1
    return (2**n)-1