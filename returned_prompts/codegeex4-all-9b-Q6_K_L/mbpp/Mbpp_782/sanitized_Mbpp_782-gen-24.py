def odd_length_sum(nums: list) -> int:
    odd_length_subarrays = []
    for i in range(len(nums)):
        for j in range(i, len(nums), 2):
            odd_length_subarrays.append(nums[i:j+1])
    return sum([sum(subarray) for subarray in odd_length_subarrays])