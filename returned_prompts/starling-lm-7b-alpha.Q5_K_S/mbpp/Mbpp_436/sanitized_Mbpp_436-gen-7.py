def neg_nos(nums):
    # Your code here
    neg_list = []
    for i in nums:
        if i < 0:
            neg_list.append(i)
    return neg_list