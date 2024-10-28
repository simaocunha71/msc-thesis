```
def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product
```
The problem is asking to write a function that takes an array of integers and an integer n, and returns the product of the array elements modulo n. 

For example, if the array is [100, 10, 5, 25, 35, 14] and n is 11, the product of the array elements is 100*10*5*25*35*14 = 35000000, and the remainder of this product divided by 11 is 9.

The function `find_remainder` calculates the product of the array elements and returns the remainder of the product divided by n. The product is calculated by multiplying each element in the array with the current product and taking the remainder of the product divided by n in each step. This way, the product does not exceed n and the remainder is calculated correctly.

The unit test `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` ensures that the function works correctly. It checks if the function returns 9 when the array is [100, 10, 5, 25, 35, 14] and n is 11. If the function returns the correct result, the test passes; otherwise, it fails. 





```
def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product
```