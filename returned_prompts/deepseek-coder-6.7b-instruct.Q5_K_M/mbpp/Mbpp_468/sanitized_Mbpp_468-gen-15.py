def max_product(arr):
    # sort the array
    arr.sort()
    # maximum product is either the product of largest two numbers or the product of three largest numbers
    return max(arr[0] * arr[1] * arr[len(arr) - 1], arr[len(arr) - 3] * arr[len(arr) - 2] * arr[len(arr) - 1])