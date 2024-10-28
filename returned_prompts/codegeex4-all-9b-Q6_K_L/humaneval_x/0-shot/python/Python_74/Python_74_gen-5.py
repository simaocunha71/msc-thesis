def total_match(lst1, lst2):
    total_chars1 = sum([len(x) for x in lst1])
    total_chars2 = sum([len(x) for x in lst2])
    if total_chars1 <= total_chars2:
        return lst1
    else:
        return lst2

print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']