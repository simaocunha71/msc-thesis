def count_Pairs(l, elem):
    n = len(l)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if l[i] != l[j] and l[i] != elem and l[j] != elem:
                count += 1
    return count

#Test
assert count_Pairs([1,2,1],3) == 2

#Test
assert count_Pairs([1,2,3,4,5], 6) == 6

#Test
assert count_Pairs([1,2,3,4,5], 1) == 8

#Test
assert count_Pairs([1,2,3], 1) == 3

#Test
assert count_Pairs([1,2,3], 2) == 3

#Test
assert count_Pairs([1,1,2], 3) == 2

#Test
assert count_Pairs([1,1,2], 2) == 2

#Test
assert count_Pairs([1,1], 2) == 0

#Test
assert count_Pairs([1], 2) == 0

#Test
assert count_Pairs([], 2) == 0

#Test
assert count_Pairs([1], 1) == 0

#Test
assert count_Pairs([], 1) == 0

#Test
assert count_Pairs([1], 1) == 0

#Test
assert count_Pairs([1], 2) == 0

#Test
assert count_Pairs([], 1) == 0

#Test
assert count_Pairs([], 2) == 0

#Test
assert count_Pairs([], 3) == 0

#Test
assert count_Pairs([], 4) == 0

#Test
assert count_Pairs([], 5) == 0

#Test
assert count_Pairs([], 6) == 0

#Test
assert count_Pairs([], 7) == 0
