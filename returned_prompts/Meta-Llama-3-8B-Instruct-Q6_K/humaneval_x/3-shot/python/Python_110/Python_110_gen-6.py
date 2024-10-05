    odd_numbers = [i for i in lst1 if i % 2 != 0]
    if len(odd_numbers) > len(lst2):
        return "NO"
    else:
        for odd in odd_numbers:
            lst2.remove(odd)
        if all(i % 2 == 0 for i in lst1):
            return "YES"
        else:
            return "NO"


