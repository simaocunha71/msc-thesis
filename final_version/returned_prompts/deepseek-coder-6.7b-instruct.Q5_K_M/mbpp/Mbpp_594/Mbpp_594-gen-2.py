def diff_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    return even - odd if even and odd else None

print(diff_even_odd([1,3,5,7,4,1,6,8]))  # 3


