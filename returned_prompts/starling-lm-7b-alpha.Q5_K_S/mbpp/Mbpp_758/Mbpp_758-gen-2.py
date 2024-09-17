
def unique_sublists(nums):
    sub_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            sub_list.append(tuple(nums[i:j]))
    sub_list_dict = {}
    for i in sub_list:
        if i not in sub_list_dict:
            sub_list_dict[i] = sub_list.count(i)
    return sub_list_dict


