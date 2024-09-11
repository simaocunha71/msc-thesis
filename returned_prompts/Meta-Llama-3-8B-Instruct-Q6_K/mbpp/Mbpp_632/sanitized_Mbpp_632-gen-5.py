def move_zero(lst):
    return [i for i in lst if i!=0] + [i for i in lst if i==0]  # or use list comprehension with if else