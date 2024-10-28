def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]  # using list comprehension
    # or
    # result = []
    # non_zero = [i for i in lst if i != 0]
    # zero = [i for i in lst if i == 0]
    # result.extend(non_zero)
    # result.extend(zero)
    # return result
    # or
    # lst.sort()
    # return [i for i in lst if i != 0] + [i for i in lst if i == 0]  # sort first, then split
    # or
    # result = []
    # for i in lst:
    #     if i != 0:
    #         result.append(i)
    # result.extend([i for i in lst if i == 0])
    # return result
    # or
    # return [i for i in lst if i != 0] + [0] * (lst.count(0) - len([i for i in lst if i != 0]))  # count zeroes
    # or
    # lst.sort(key=lambda x:0 if x!=0 else 1)  # sort with 0 as first priority
    # return lst
    # or
    # result = []
    # for i in lst:
    #     if i != 0:
    #         result.append(i)
    # return result + [i for i in lst if i == 0]  # append zeroes at the end
    # or
    # return [i for i in lst if i != 0] + [i for i in lst if i == 0]  # split list into two parts, then concatenate
    # or
    # result = []
    # for i in lst:
    #     if i != 0:
    #         result.append(i)
    #     else:
    #         result.append(i)
    # return result  # append zeroes as they are
    # or
    # return [i for i in lst if i != 0] + [0] * len([i for i in lst if i == 0])  # append zeroes at the end
    # or
    # result = []
    # for i in lst:
    #     if i != 0:
    #         result