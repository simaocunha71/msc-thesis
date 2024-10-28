def move_one_ball(arr):
    if len(arr)==0:
        return True
    arr.sort()
    for i in range(len(arr)):
        if arr[i]!=arr[0]:
            break
    else:
        return True
    arr=arr[i:]+arr[:i]
    for i in range(len(arr)):
        if arr[i]!=arr[0]:
            break
    else:
        return True
    return False


print(move_one_ball([3, 4, 5, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2, 4]))
print(move_one_ball([3, 5, 4, 1, 2, 3]))
print(move_one_ball([1, 2, 3, 4, 5]))
print(move_one_ball([5, 4, 3, 2, 1]))
print(move_one_ball([3, 4, 5, 1, 2, 5]))
print(move_one_ball([3, 4, 5, 1, 2, 6]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7, 8]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7, 8, 9]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7, 8, 9, 10]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7, 8, 9, 10, 11]))
print(move_one_ball([3, 4, 5, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12]))
print(move_one_ball([3, 4, 5, 1, 2, 