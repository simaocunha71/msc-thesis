def get_pairs_count(arr, sum):
    map = {}
    twice_count = 0
    for i in range(0, len(arr)):
        if sum - arr[i] in map:
            twice_count += map[sum - arr[i]]
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    return twice_count

print(get_pairs_count([1,1,1,1],2)) # 6

Explanation:
In this function, we iterate over the given list of numbers. For each number, we check if its complement (the number we need to add up to the given sum) is already present in the map. If it is, we add the count of its complement to the total count of pairs.
Next, we check if the current number is already present in the map. If it is, we increment its count by 1. If it is not, we add it to the map with a count of 1.
Finally, we return the total count of pairs.
"""

"""
