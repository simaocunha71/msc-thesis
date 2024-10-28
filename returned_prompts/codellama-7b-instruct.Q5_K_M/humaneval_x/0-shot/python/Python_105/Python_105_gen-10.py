
def by_length(arr):
    # return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i-1] for i in arr if 1 <= i <= 9]