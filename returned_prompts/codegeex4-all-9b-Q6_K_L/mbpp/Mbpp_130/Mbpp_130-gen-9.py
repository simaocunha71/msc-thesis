def max_occurrences(nums: list) -> int:
    count_dict = {}
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    max_count = max(count_dict.values())
    for key, value in count_dict.items():
        if value == max_count:
            return key

