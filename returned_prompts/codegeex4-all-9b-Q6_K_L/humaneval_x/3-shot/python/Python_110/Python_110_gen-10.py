    def count_even_numbers(lst):
        return sum(1 for num in lst if num % 2 == 0)

    even_numbers_in_lst1 = count_even_numbers(lst1)
    even_numbers_in_lst2 = count_even_numbers(lst2)

    if even_numbers_in_lst1 + even_numbers_in_lst2 == len(lst1):
        return "YES"
    else:
        return "NO"

