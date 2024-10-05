
def by_length(arr):
    if not arr:
        return []
    arr = sorted(filter(lambda x: x >= 1 and x <= 9, arr))
    arr.reverse()
    return [names[x] for x in arr]

    # names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
