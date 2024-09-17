```
def find_remainder(arr, n):
    product = 1
    for i in arr:
        product = (product * i) % n
    return product
```


The function `find_remainder` takes a list of integers `arr` and an integer `n` as input. It initializes a variable `product` to 1, then iterates over each element in the list. For each element, it calculates the product modulo `n` and assigns the result back to `product`. Finally, it returns the product.

The unit test `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` ensures that the function works correctly by comparing the result with the expected output. In this case, the expected output is 9, which is the product of the array elements modulo 11. The actual output of the function will be the same as the expected output because the function uses the modulo operator to ensure the result stays within the range of `n`. 

For example, if the product is 1210, the function will calculate the remainder of 1210 divided by 11, which is 9. This ensures that the result is always within the range of `n` and prevents overflow. 

This function is efficient because it uses the modulo operator to reduce the product at each step, which reduces the risk of overflow. It also has a time complexity of O(n), where n is the length of the input list, because it needs to iterate over each element in the list. 

However, the function assumes that the input list contains only positive integers. If the list contains negative integers or non-integer values, the function may not work correctly. Also, if `n` is 0, the function will raise a ZeroDivisionError when it tries to calculate the remainder. To handle these edge cases, additional error checking and handling code would be needed. 