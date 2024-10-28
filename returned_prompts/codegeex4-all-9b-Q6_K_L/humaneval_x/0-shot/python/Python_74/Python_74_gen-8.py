def total_match(lst1, lst2):
    lst1_total = sum(len(s) for s in lst1)
    lst2_total = sum(len(s) for s in lst2)
    if lst1_total == lst2_total:
        return lst1
    elif lst1_total < lst2_total:
        return lst1
    else:
        return lst2

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))