def get_pairs_count(arr, sum):
    map = {}
    twice_count = 0
    for i in range(0, len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    for i in range(0, len(arr)):
        twice_count += map[sum - arr[i]]
        if (sum - arr[i]) == arr[i]:
            twice_count -= 1
    return int(twice_count / 2)