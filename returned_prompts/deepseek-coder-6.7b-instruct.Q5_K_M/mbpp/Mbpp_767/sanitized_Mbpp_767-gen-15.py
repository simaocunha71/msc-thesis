def get_pairs_count(arr, sum):
    n = len(arr)
    m = [0] * 1000
    twice_count = 0
    for i in range(0, n):
        if (arr[i] < sum):
            m[arr[i]] += 1

    for i in range(0, n):
        twice_count += m[sum - arr[i]]
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    return int(twice_count / 2)