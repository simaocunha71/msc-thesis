
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            if str(num)[0] in ['1', '3', '5', '7', '9']:
                if str(num)[-1] in ['1', '3', '5', '7', '9']:
                    count += 1
    return count


