```
def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product
```
This function takes two parameters, an array of numbers and an integer n. It initializes a product variable to 1, then iterates over each number in the array. For each number, it multiplies the product by the number, and takes the remainder of the result when divided by n. Finally, it returns the product. 

The unit test `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` ensures that the function works correctly. 

This function can be used to find the product of the array elements modulo n. For example, if you want to find the product of the array elements modulo 11, you can call `find_remainder([ 100, 10, 5, 25, 35, 14 ],11)`. 

The time complexity of this function is O(n), where n is the number of elements in the array, because it needs to iterate over each element in the array once. The space complexity is O(1), because it only uses a constant amount of space to store the product and the remainder. 