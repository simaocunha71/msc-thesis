from itertools import chain
def two_unique_nums(nums_list):
    return list(set(chain(*nums_list)))
    #return list(set([i for sub_list in nums_list for i in sub_list]))
    #return list(set([i for nums in nums_list for i in nums if nums_list.count(i) == 1]))
    #return sorted(set([i for nums in nums_list for i in nums if nums_list.count(i) == 1]))