
def total_match(lst1, lst2):
    total_len1 = sum(len(i) for i in lst1)
    total_len2 = sum(len(i) for i in lst2)
    if total_len1 < total_len2:
        return lst1
    elif total_len1 > total_len2:
        return lst2
    else:
        return lst1

print(total_match([], [])) # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) # ➞ ['4']

# The function works by first calculating the total length of each list by adding up the length of each string in the list. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list.
<jupyter_output>
[]
['hI', 'Hi']
['hi', 'admin']
['hI', 'hi', 'hi']
['4']
<jupyter_text>
