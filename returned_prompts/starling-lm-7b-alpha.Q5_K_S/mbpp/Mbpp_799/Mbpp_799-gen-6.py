```
def left_rotate(n,d):
    '''
    Rotate left bits by d bits a given number. We assume that the number is 32 bit.
    '''
    return ((n<<d)%(2**32)) | (n>>32-d)
```

Explanation:

The `left_rotate` function takes in two parameters: `n` and `d`. `n` is the number that we want to rotate the bits of and `d` is the number of positions to rotate the bits to the left by. 

In the function, we use the left shift operator (`<<`) to shift the bits of `n` to the left by `d` positions. We also use the modulo operator (`%`) to ensure that the result is within the range of 32 bits. 

Next, we use the bitwise OR operator (`|`) to combine the shifted bits with the rightmost `32-d` bits of `n`. This ensures that all the bits are shifted to the left by `d` positions without losing any bits. 

The function then returns the result of the rotation.

To test the function, we can use the `assert` statement to check if the result of rotating the bits of 16 by 2 is equal to 64. This will pass if the function is working correctly.

The time complexity of this function is O(1) because the operations performed are constant time.

The space complexity is also O(1) because the function does not require any additional space that scales with the size of the input.

Overall, this function provides a simple and efficient solution to rotate left bits of a given number by a specified number of positions.

The time complexity of this function is O(1) because the operations performed are constant time. 

The space complexity is also O(1) because the function does not require any additional space that scales with the size of the input. 

Overall, this function provides a simple and efficient solution to rotate left bits of a given number by a specified number of positions. 

```python
def left_rotate(n,d):
    '''
    Rotate left bits by d bits a given number. We assume that the number is 32 bit.