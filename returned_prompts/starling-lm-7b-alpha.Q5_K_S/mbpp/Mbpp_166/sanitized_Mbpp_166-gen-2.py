def find_even_pair(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 0:
                result += 1
    return result