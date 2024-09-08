def find_even_pair(nums):
    from itertools import combinations
    count = 0
    for pair in combinations(nums, 2):
        if pair[0] ^ pair[1] % 2 == 0:
            count += 1
    return count