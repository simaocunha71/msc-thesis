
def big_diff(lst):
    if not lst:
        return 0
    return max(lst) - min(lst)

print(big_diff([1,2,3,4])) # should return 3


