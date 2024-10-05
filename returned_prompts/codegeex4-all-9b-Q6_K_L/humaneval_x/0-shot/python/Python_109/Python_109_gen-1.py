def move_one_ball(arr):
    if len(arr) == 0:
        return True
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    if max_index == len(arr)-1 and min_index == 0:
        return True
    if max_index < min_index:
        min_index -= 1
    if len(arr) % min_index == 0:
        return True
    else:
        return False

print(move_one_ball([3, 4, 5, 1, 2])) #==>True
print(move_one_ball([3, 5, 4, 1, 2])) #==>False
print(move_one_ball([1, 2, 3, 4, 5])) #==>True
print(move_one_ball([5, 4, 3, 2, 1])) #==>True
print(move_one_ball([])) #==>True