    even_numbers = [x for x in lst1 if x % 2 == 0]
    odd_numbers = [x for x in lst1 if x % 2 != 0]
    even_numbers_in_lst2 = [x for x in lst2 if x % 2 == 0]

    if len(even_numbers) + len(even_numbers_in_lst2) >= len(odd_numbers):
        return "YES"
    else:
        return "NO"

