
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return True
        else:
            return False

    if len(arr) > 2:
        count = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                count = count + 1
                if count == 1:
                    arr.insert(0, arr.pop())
        if count == 0:
            return True
        else:
            return False
