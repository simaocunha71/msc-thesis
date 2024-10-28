
def pluck(arr):
    if not arr:
        return []
    even_vals = [x for x in arr if x % 2 == 0]
    if not even_vals:
        return []
    return [min(even_vals, key=lambda x: x % 2), even_vals.index(min(even_vals, key=lambda x: x % 2))]

def pluck(arr):
    if not arr:
        return []
    even_vals = [x for x in arr if x % 2 == 0]
    if not even_vals:
        return []
    return [min(even_vals, key=lambda x: x % 2), even_vals.index(min(even_vals, key=lambda x: x % 2))]


