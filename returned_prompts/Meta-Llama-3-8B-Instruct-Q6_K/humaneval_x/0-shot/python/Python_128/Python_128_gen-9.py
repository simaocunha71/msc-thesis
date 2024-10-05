```
def prod_signs(arr):
    if not arr:
        return None
    sign_product = 1
    for num in arr:
        sign_product *= 1 if num >= 0 else -1
    return sum(abs(num) for num in arr) * sign_product
```
This function first checks if the input array is empty. If it is, the function returns None. If the array is not empty, the function initializes a variable sign_product to 1. Then, it iterates over each number in the array, multiplying sign_product by 1 if the number is non-negative and by -1 if the number is negative. This way, sign_product is set to the product of all signs in the array. Finally, the function returns the sum of the magnitudes of all numbers in the array (obtained using the abs function) multiplied by the sign_product. This result is the sum of magnitudes of integers multiplied by product of all signs of each number in the array.