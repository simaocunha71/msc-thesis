
def get_pairs_count(arr, sum):
    n = len(arr)
    m = [0] * 1000
    twice_count = 0
    for i in range(0, n):
        if (arr[i] * 2 == sum):
            twice_count += 1
        m[arr[i]] += 1
    pair_count = 0
    for i in range(0, n):
        pair_count += m[sum - arr[i]]
        if (sum - arr[i] == arr[i]):
            pair_count -= 1
    return int(pair_count / 2 + twice_count)


