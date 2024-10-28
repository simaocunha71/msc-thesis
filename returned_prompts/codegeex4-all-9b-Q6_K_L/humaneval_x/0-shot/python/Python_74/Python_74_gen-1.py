def total_match(lst1, lst2):
    def total_chars(lst):
        return sum(len(s) for s in lst)
    if total_chars(lst1) <= total_chars(lst2):
        return lst1
    else:
        return lst2

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
