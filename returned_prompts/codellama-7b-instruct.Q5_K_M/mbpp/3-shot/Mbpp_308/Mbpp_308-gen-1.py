
def large_product(list1, list2, n):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    res = []
    for _ in range(n):
        res.append(list1.pop() * list2.pop())
    return res


