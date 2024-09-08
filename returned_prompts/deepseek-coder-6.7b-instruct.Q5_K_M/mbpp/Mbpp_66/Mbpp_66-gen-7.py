def pos_count(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4])) # 2


"""
