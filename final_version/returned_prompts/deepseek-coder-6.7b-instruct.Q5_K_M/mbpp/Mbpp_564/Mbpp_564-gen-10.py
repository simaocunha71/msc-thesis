
def count_Pairs(lst,n):
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if lst[i] != lst[j]:
                pairs += 1
    return pairs

print(count_Pairs([1,2,1],3)) # 2

"""
Explanation:
The function takes a list and its length as parameters. It then iterates over the list in pairs, counting the pairs where the elements are unequal.
"""
<jupyter_output>
2
<jupyter_text>
Problem 2: Write a python function that takes a list of strings and returns a dictionary where the keys are the strings and the values are the counts of each string.
<jupyter_code>
