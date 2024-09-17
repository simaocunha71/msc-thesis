from collections import Counter
def validate(nums):
    cnt = Counter(str(nums))
    for i in cnt:
        if cnt[i] > int(i):
            return False
    return True