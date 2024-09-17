def sum_Of_Subarray_Prod(list):
    if not list:
        return 0
    n = len(list)
    result = 0
    for i in range(n):
        for j in range(i+1, n+1):
            result += sum(list[i:j]) * (j-i)
    return result