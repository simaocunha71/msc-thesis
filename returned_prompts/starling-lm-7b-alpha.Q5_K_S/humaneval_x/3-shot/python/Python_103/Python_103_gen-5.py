    if n > m:
        return -1
    nums = list(range(n, m + 1))
    avg = sum(nums) / len(nums)
    binary = bin(round(avg))[2:]
    if len(binary) < len(str(m)):
        binary = '0' * (len(str(m)) - len(binary)) + binary
    return binary


