
def search(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    return search(arr[1:])


