```
def find_remainder(arr,n):
    product=1
    for i in arr:
        product=(product*i)%n
    return product
```


The problem is asking for a function that calculates the product of all the elements in a given array, and then finds the remainder of this product when divided by a given number `n`. 

The unit test provided, `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9`, helps to clarify this by showing that the function should return the remainder of the product when divided by 11.

The solution provided uses a simple loop to calculate the product of all elements in the array, and then finds the remainder of this product when divided by `n`. This is done using the modulo operator `%`. The function returns the calculated remainder.

For example, if we call `find_remainder([ 100, 10, 5, 25, 35, 14 ],11)`, the function will calculate the product of all elements in the array (which is 125000000), and then find the remainder of this product when divided by 11 (which is 9). Therefore, the function will return `9`. 