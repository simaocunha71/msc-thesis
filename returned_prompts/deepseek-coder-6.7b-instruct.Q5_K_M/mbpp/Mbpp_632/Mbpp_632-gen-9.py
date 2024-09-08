def move_zero(lst):
    return [num for num in lst if num != 0] + [0] * lst.count(0)

print(move_zero([1,0,2,0,3,4]))

