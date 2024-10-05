def pluck(arr):
    evens = [i for i in enumerate(arr) if i[1] % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens, key=lambda x: (x[1], x[0]))
    return [smallest_even[1], smallest_even[0]]