def move_one_ball(arr):
    return sorted(arr) == arr or arr == sorted(arr, reverse=True)

