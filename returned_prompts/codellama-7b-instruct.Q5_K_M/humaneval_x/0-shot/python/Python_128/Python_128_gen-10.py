
def prod_signs(arr):
    product = 1
    total = 0
    for num in arr:
        product *= num
        total += abs(num)
    return total * product if product != 0 else None
