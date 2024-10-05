    lst1_evens = [n for n in lst1 if n % 2 == 0]
    lst2_odds = [n for n in lst2 if n % 2 != 0]

    if len(lst1_evens) == len(lst1) and len(lst2_odds) == len(lst2):
        return "YES"
    else:
        return "NO"

