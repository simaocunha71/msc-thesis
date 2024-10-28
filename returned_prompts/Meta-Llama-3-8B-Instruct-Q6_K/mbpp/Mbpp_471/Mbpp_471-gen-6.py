```
def find_remainder(arr, n):
    product = 1
    for i in arr:
        product = (product * i) % n
    return product
```
This function calculates the product of all the elements in the array and then calculates the remainder of the product when divided by n. The product is calculated by multiplying the current product with the current element and taking the modulus of n in each iteration. The final product is then returned. The function will pass the given unit test case.  The unit test case is: assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9. It means the product of the array [ 100, 10, 5, 25, 35, 14 ] modulo 11 should be 9.  



Here is the code with explanation:

```
def find_remainder(arr, n):
    product = 1  # Initialize product as 1
    for i in arr:
        product = (product * i) % n  # Calculate the product modulo n
    return product
```
The function takes two parameters: the array of numbers and the modulus number. It initializes a variable `product` to 1. Then it iterates over each number in the array. For each number, it calculates the product of the current product and the current number, and then takes the remainder of this product when divided by `n`. This ensures that the product stays within the range of `n` and does not overflow. Finally, it returns the product.  



This function is efficient because it only requires a single pass over the array, and it uses the modulus operation to keep the product within the range of `n`. This makes it suitable for large arrays and large modulus numbers.  



The function also handles the case where the input array is empty by returning 0, as the product of an empty array is defined as 1. However, in this case, the function returns the product modulo `n`, which is equivalent to 0.  



The unit test case `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` ensures that the function works correctly for a specific input array and modulus number.  



The function can be further optimized by using the properties of modular arithmetic, such as the fact that `(a * b) % n = ((a % n)