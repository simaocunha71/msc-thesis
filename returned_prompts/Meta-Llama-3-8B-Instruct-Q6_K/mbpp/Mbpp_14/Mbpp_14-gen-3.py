```
def find_Volume(base, height, length):
    return 0.5 * base * height * length
```
This function takes three parameters: base, height, and length. The formula for the volume of a triangular prism is (1/2) * base * height * length. This function returns the calculated volume. 

The unit test `assert find_Volume(10,8,6) == 240` ensures that the function is working correctly. The function returns 240 when the base is 10, the height is 8, and the length is 6, which is the correct volume for a triangular prism with these dimensions. 