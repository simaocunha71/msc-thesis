    from collections import Counter
    from operator import itemgetter

    def search(lst):
        c = Counter(lst)
        if len(lst) == 1:
            return -1
        max_ele = max(lst)
        max_val = max(c.values())
        for i in range(max_ele, 0, -1):
            if c[i] >= i:
                return i
        return -1


# print(search([4, 1, 2, 2, 3, 1]))  # 2
# print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
# print(search([5, 5, 4, 4, 4]))  # -1


# def search(lst):
#     lst.sort()
#     for i in range(len(lst) - 1, 0, -1):
#         if lst[i] == lst[i - 1]:
#             continue
#         elif lst[i] > lst[i - 1]:
#             return lst[i - 1]
#         else:
#             break
#     return -1


# print(search([4, 1, 2, 2, 3, 1]))  # 2
# print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # 3
# print(search([5, 5, 4, 4, 4]))  # -1


# def search(lst):
#     c = Counter(lst)
#     if len(lst) == 1:
#         return -1
#     max_ele = max(c)
#     max_val = max(c.values())
#     for i in range(max_ele, 0, -1):
#         if c[i] >= i:
#             return i
#     return -1


# print(search([4, 1, 2, 2, 3