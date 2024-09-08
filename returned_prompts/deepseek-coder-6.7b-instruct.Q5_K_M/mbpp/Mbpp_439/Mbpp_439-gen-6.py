
def multiple_to_single(nums):
    res = ''.join(map(str, nums))
    return int(res)

print(multiple_to_single([11, 33, 50]))  # 113350



