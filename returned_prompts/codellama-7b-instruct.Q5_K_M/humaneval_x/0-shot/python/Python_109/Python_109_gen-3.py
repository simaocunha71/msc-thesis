
def move_one_ball(arr):
    # Write your code here
    if len(arr) == 0:
        return True
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False
    return True



