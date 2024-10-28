
def pair_xor_Sum(arr: list) -> int:
    return sum(a^b for a,b in zip(arr,arr[1:]))


