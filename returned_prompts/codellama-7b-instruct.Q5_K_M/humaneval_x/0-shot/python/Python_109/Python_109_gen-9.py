
def move_one_ball(arr):
    # Write your code here
    arr.sort()
    return True if arr==sorted(arr) else False
