def consecutive_duplicates(lst):
    return [i for n, i in enumerate(lst) if i not in lst[n+1:]]
    # or
    # return list(dict.fromkeys(lst))
    # or
    # return [i for i in lst if lst.count(i) == 1]  # this will not work correctly for lists with duplicates and non-duplicates
    # or
    # result = []
    # for i in lst:
    #     if i not in result:
    #         result.append(i)
    # return result
    # or
    # return [x for i,x in enumerate(lst) if lst[i:] != [x]*len(lst[i:])].tolist()  # this will not work correctly for lists with duplicates and non-duplicates
    # or
    # result = []
    # for i in lst:
    #     if i not in result:
    #         result.append(i)
    #     else:
    #         if result[-1] != i:
    #             result.append(i)
    # return result
    # or
    # return [i for i in lst if i not in lst[lst.index(i)+1:]]
    # or
    # return list(dict((k, i) for k, i in enumerate(lst)))
    # or
    # return list(dict.fromkeys([i for n, i in enumerate(lst) if i not in lst[n+1:]]))
    # or
    # return [i for i in lst if lst.index(i) == lst.index(i)]
    # or
    # return [i for i in lst if lst.count(i) == 1]
    # or
    # return list(dict((k, i) for k, i in enumerate(lst) if i not in lst[k+1:]))
    # or
    # return list(dict.fromkeys([i for i in lst if i not in lst[lst.index(i)+1:]]))
    # or
    # return [i for i in lst if i not in [j for j in lst if j != i]]
    # or
    # return list(dict((k, i) for k, i in enumerate(lst) if i not in [j for j in lst if j != i]))
    # or
    # return list(dict.fromkeys([i for i in lst if i not in [j for j in lst if j != i]]))



Note: This