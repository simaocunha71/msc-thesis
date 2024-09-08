
def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3)) # 2


"""
Explanation:

In the given list [1,2,1], there are 3 elements. 

There are 3 pairs of unordered elements: (1,2), (1,1), (2,1).

There are 2 pairs where both elements are unequal: (1,2), (2,1).

So, the function count_Pairs([1,2,1],3) returns 2.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
