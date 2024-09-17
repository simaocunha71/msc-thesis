
def get_lucid(n):
    lucid_nums = []
    for i in range(1,n+1):
        lucid_nums.append(i)
        if lucid_nums[-1] not in lucid_nums:
            lucid_nums.remove(lucid_nums[-1])
    return lucid_nums


