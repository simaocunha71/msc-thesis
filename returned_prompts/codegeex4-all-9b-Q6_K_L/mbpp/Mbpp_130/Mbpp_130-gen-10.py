def max_occurrences(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    max_freq = max(counter.values())
    for num, freq in counter.items():
        if freq == max_freq:
            return num

