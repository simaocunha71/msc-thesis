
def total_match(lst1, lst2):
    total1 = sum(len(string) for string in lst1)
    total2 = sum(len(string) for string in lst2)
    
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        return lst1

print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']

In this code, we first calculate the total number of characters in each list by summing the lengths of the strings in the list. We then compare these totals and return the list with the smaller total. If the totals are equal, we return the first list.
