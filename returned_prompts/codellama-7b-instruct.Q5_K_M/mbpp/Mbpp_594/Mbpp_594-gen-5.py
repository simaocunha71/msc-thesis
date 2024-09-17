
def diff_even_odd(my_list):
    even, odd = next((x for x in my_list if x % 2 == 0), None), next((x for x in my_list if x % 2 == 1), None)
    if even and odd:
        return even - odd
    else:
        return None


