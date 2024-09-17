def find_even_pair(nums):
    count = 0
    seen = set()
    for num in nums:
        for other in nums:
            if num != other and (num ^ other) % 2 == 0 and num not in seen and other not in seen:
                count += 1
                seen.add(num)
                seen.add(other)
    return count