def max_occurrences(nums):
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return max(counter, key=counter.get)