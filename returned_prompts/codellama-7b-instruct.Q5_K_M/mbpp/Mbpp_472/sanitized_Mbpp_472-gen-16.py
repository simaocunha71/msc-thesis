def check_Consecutive(arr: list) -> bool:
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] != 1:
            return False
    return True