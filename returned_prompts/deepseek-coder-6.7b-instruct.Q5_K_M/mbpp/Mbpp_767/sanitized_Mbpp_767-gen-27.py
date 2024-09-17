def get_pairs_count(arr, sum):
    n = len(arr)
    m = [0] * 1000
    twosum = 0
    for i in range(0, n):
        twosum = sum - arr[i]
        if (twosum >= 0):
            m[twosum] += 1
    count = 0
    for i in range(0, len(m)):
        if (m[i] > 1):
            count += int(m[i]*(m[i]-1)/2)
    return count