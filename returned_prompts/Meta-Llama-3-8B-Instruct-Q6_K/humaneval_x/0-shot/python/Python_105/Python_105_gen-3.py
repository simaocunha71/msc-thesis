```
def by_length(arr):
    if not arr:
        return []

    arr = [num for num in arr if 1 <= num <= 9]
    arr.sort()
    arr = arr[::-1]
    return [f"{'Zero' if num == 0 else 'One' if num == 1 else 'Two' if num == 2 else 'Three' if num == 3 else 'Four' if num == 4 else 'Five' if num == 5 else 'Six' if num == 6 else 'Seven' if num == 7 else 'Eight' if num == 8 else 'Nine'}" for num in arr]
``` 