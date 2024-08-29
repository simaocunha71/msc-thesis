def prod_signs(arr):
    if not arr:
        return -32768
    else:
        prod = 1
        for i in arr:
            if i<0:
                prod *= -1
            elif i==0:
                prod = 0
                break
            else:
                prod *= 1
        return prod

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))

