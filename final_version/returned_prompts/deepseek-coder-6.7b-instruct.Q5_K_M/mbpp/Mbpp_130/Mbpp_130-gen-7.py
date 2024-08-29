def max_occurrences(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return max(count, key=count.get)

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))


"""
