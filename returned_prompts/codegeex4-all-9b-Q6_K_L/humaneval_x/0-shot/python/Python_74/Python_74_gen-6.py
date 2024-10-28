def total_match(lst1, lst2):
    len1 = len(''.join(lst1))
    len2 = len(''.join(lst2))
    if len1 < len2:
        return lst1
    elif len2 < len1:
        return lst2
    else:
        return lst1

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))