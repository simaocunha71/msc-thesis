
def pluck(arr):
    if not arr:
        return []

    min_even = min(i for i in arr if i % 2 == 0)
    min_even_index = arr.index(min_even)
    return [min_even, min_even_index]



