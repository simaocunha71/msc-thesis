
def max_product(arr: list) -> tuple:
    n = len(arr)
    if n == 0:
        return (0, 0)
    max_x = max_y = arr[0]
    for i in range(1, n):
        x, y = arr[i], max_x
        if y * arr[i] < x * arr[i]:
            max_x, max_y = x, y
    return (max_x, max_y)


