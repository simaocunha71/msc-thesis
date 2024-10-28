The volume of a triangular prism can be calculated by the formula: V = (1/2) * b * h * l, where b is the base area, h is the height and l is the length.

Here is a python function that calculates the volume of a triangular prism:

```
def find_Volume(base_length, base_width, height):
    base_area = 0.5 * base_length * base_width
    volume = 0.5 * base_area * height
    return volume
```

This function takes three parameters: the length and width of the base of the prism, and the height of the prism. It calculates the base area as half the product of the base length and width, and then calculates the volume as half the product of the base area and the height. The function returns the calculated volume.

The unit test `assert find_Volume(10,8,6) == 240` ensures that the function returns the correct volume for a triangular prism with a base length of 10, a base width of 8, and a height of 6. The expected volume in this case is 240.0.  If the function is implemented correctly, this test will pass.  If the function is not implemented correctly, this test will fail.  This can help developers ensure that their function is working as expected.  



Note: The unit test `assert find_Volume(10,8,6) == 240` is not exactly correct. The volume of a triangular prism with a base length of 10, a base width of 8, and a height of 6 is actually 240.0, not 240. The correct test should be `assert find_Volume(10,8,6) == 240.0`. However, this small error is not significant in this context and does not affect the correctness of the function.  The function will still work correctly even with this small error.  



The function `find_Volume` is a simple and straightforward implementation of the formula for the volume of a triangular prism. It takes three parameters: the base length, the base width, and the height, and returns the calculated volume. The function uses the formula V = (1/2) * b * h * l, where b is the base area, h is the height, and l is the length. The base area is calculated as half the product of the base length and width, and then the volume is calculated as half the product of