def convert_list_dictionary(nums,names,scores):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = {}
        d[nums[i]][names[i]] = scores[i]
    return d