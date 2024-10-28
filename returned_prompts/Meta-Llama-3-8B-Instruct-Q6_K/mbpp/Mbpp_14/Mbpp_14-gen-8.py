```
def find_Volume(base, height, length):
    return 0.5 * base * height * length
```
This function takes three parameters: base, height, and length, which are the base of the triangle, the height of the triangle, and the length of the prism, respectively. The function calculates the volume of the triangular prism using the formula: V = (1/2) * base * height * length, and returns the result. The unit test `assert find_Volume(10,8,6) == 240` shows that the function is working correctly. 

The volume of a triangular prism is the area of the base (a triangle) multiplied by the height of the prism. The area of a triangle can be calculated using the formula: A = (1/2) * base * height, where base is the length of the base of the triangle, and height is the height of the triangle. Therefore, the volume of a triangular prism is: V = A * height = (1/2) * base * height * height. 

However, in the problem statement, the length of the prism is given, not the height. So, we can use the formula: V = (1/2) * base * height * length, where base is the length of the base of the triangle, height is the height of the triangle, and length is the length of the prism. This is the formula used in the function above. 

The function is tested with the unit test `assert find_Volume(10,8,6) == 240`, which shows that the function is working correctly. The expected result is 240, which is the volume of a triangular prism with a base of 10, a height of 8, and a length of 6. The actual result of the function is 240, so the function is correct. 