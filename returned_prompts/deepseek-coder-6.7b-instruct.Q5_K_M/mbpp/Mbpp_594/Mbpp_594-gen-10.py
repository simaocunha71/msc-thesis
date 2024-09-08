def diff_even_odd(lst):
    even_num = [i for i in lst if i % 2 == 0]
    odd_num = [i for i in lst if i % 2 != 0]
    return even_num[0] - odd_num[0]

print(diff_even_odd([1,3,5,7,4,1,6,8]))


