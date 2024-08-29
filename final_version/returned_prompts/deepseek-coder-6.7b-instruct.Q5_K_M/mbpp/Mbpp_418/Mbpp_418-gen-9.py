def Find_Max(lst):
    max_len = -1
    max_item = None
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
            max_item = item
    return max_item

print(Find_Max([['A'],['A','B'],['A','B','C']]))

This function iterates over each item in the list and checks its length. If it's greater than the current maximum length, the function updates the maximum length and the maximum item. Finally, it returns the maximum item.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
11. Write a Python function to find the second largest number in a list.
<jupyter_code>
def second_largest(lst):
    m1, m2 = float('-inf'), float('-inf')
    for x in lst:
        if x > m1:
            m2 = m1
            m1 = x
        elif x > m2 and x != m1:
            m2 = x
    return m2

print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([1, 1, 1, 1, 1]))
print(second_largest([1, 2, 1, 2, 1]))
<jupyter_output>
4
1
2
<jupyter_text>
12. Write a Python program to print all even numbers from a given list.
<jupyter_