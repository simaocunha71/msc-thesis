def find_even_pair(nums):
    even_pairs = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                even_pairs += 1
    return even_pairs