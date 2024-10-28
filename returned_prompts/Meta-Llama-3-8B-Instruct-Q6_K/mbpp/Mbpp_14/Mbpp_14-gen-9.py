```
def find_Volume(base, height, length):
    return 0.5 * base * height * length
```


The function find_Volume calculates the volume of a triangular prism given the base, height, and length. The volume of a triangular prism is calculated by multiplying the area of the triangle (0.5 * base * height) by the length. The unit test provided, assert find_Volume(10,8,6) == 240, suggests that the function should return a value of 240 when the base is 10, height is 8, and length is 6. This is the expected result given these dimensions. 
The unit test is used to verify that the function is working correctly. It is a good practice to include unit tests when writing functions to ensure that the function behaves as expected. 