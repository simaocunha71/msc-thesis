
def move_one_ball(arr):
    # Write your code here
    if not arr:
        return True
    arr.sort()
    if arr == list(range(1, len(arr) + 1)):
        return True
    return False
