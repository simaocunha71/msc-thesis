
def pair_xor_Sum(arr: list, n: int) -> int:
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            result = result + arr[i] ^ arr[j]
    return result


