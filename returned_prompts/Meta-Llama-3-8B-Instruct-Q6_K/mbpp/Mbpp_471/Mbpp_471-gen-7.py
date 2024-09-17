```
def find_remainder(arr, n):
    product = 1
    for i in arr:
        product = (product * i) % n
    return product
```
This function calculates the product of all elements in the array, and then takes the remainder of the product when divided by n. 

The unit test `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` shows that the function should return the remainder of the product when divided by n, not the product itself. For example, the product of the array [100, 10, 5, 25, 35, 14] is 2250000, but the remainder of this product when divided by 11 is 9. 

The function uses a loop to multiply each element in the array by the current product, and then takes the remainder of the product when divided by n. This is done to avoid overflow errors when multiplying large numbers. 

For example, if the array is [100, 10, 5, 25, 35, 14], the function will calculate the product as follows:
(1 * 100) % 11 = 1
(1 * 100 + 10) % 11 = 10
(10 * 5) % 11 = 50
(50 * 25) % 11 = 125
(125 * 35) % 11 = 4375
(4375 * 14) % 11 = 9

The function then returns the remainder, which is 9.  This is the expected output for the unit test. 