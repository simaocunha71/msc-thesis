from collections import Counter
def validate(nums):
    cnt = Counter(str(nums))
    for i in cnt:
        if cnt[i] > int(i):
            return False
    return True

# Alternate Solution
def validate(nums):
    return all(i <= cnt[str(i)] for i in range(10))

# Another alternate solution
def validate(nums):
    return all(str(i) * cnt[str(i)] <= str(nums) for i in range(10))

# Yet another alternate solution
def validate(nums):
    f = {str(i):0 for i in range(10)}
    for i in str(nums):
        f[i] += 1
    return all(f[str(i)] <= int(i) for i in range(10))

# Yet another alternate solution
def validate(nums):
    return all(str(i) * cnt[str(i)] <= str(nums) for i in range(10))

# Yet another alternate solution
def validate(nums):
    freq = Counter(str(nums))
    return all(freq[str(i)] <= int(i) for i in range(10))

# Yet another alternate solution
def validate(nums):
    return all(str(i) * cnt[str(i)] <= str(nums) for i in range(10))

# Yet another alternate solution
def validate(nums):
    return all(str(i) * cnt[str(i)] <= str(nums) for i in range(10))

"""
Example:
>>> validate(1234)
True
>>> validate(1000)
True
>>> validate(123)
True
>>> validate(12345)
True
>>> validate(123456)
True
>>> validate(1234567)
True
>>> validate(1234568)
False
>>> validate(1234569)
False
>>> validate(123457)
False
>>> validate(1234