def find_even_pair(nums):
    count = 0
    seen = set()
    for num in nums:
        for seen_num in seen:
            if (num ^ seen_num) % 2 == 0:
                count += 1
        seen.add(num)
    return count