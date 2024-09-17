def odd_length_sum(nums: list) -> int:
    sum = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum += sum(nums[:i+1])
    return sum