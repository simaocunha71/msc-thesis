    even_count = sum(1 for num in lst1 if num % 2 == 0)
    odd_count = len(lst1) - even_count

    even_count_2 = sum(1 for num in lst2 if num % 2 == 0)
    odd_count_2 = len(lst2) - even_count_2

    if even_count + odd_count_2 >= len(lst1):
        return "YES"
    else:
        return "NO"

