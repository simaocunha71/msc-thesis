def max_occurrences(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # Find the number with maximum frequency
    max_freq = 0
    max_num = None
    for num, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_num = num

    return max_num