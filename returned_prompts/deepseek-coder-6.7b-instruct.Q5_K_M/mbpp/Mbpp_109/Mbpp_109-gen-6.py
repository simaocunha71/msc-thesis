
def odd_Equivalent(s,n):
    binary_num = bin(int(s, 2) * int('1'+'0'*(n-1), 2))[2:]
    binary_num = (binary_num+'0'*n)[:len(binary_num)]
    return sum(int(binary_num[i] != binary_num[i-1]) for i in range(1, len(binary_num)))


