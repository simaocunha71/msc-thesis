def common_Elements(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

print(common_Elements([1,2,3],[1,2,4],[1,5,2]))

"""
Explanation:
The function `common_Elements` takes three lists `lst1`, `lst2`, and `lst3` as arguments. It converts each list to a set and finds the