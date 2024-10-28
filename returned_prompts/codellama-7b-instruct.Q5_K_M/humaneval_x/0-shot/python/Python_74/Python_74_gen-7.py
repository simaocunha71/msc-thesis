
def total_match(lst1, lst2):
    if not lst1 or not lst2:
        return []

    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)

    if total1 == total2:
        return lst1
    elif total1 < total2:
        return lst1
    else:
        return lst2

total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
