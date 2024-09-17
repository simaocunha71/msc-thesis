def find_even_pair(nums):
    num_set = set(nums)
    count = 0
    for num in num_set:
        complement = num ^ (num - 1)
        count += num_set.count(complement)
    return count // 2