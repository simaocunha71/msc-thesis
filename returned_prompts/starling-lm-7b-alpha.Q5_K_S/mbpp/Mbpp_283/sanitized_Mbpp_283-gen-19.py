def validate(num):
    nums = [int(i) for i in str(num)]
    for num in nums:
        if nums.count(num) > num:
            return False
    return True