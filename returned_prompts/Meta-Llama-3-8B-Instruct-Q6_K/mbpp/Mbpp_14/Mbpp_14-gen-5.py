```
def find_Volume(base, height, width):
    return (base * height * width) / 2
```
The volume of a triangular prism can be calculated by multiplying the base area of the triangle with the height and dividing by 2. The base area of the triangle can be calculated by multiplying the base with the height. 

In the given problem, the function find_Volume takes three parameters: base, height, and width. It returns the volume of the triangular prism. The unit test `assert find_Volume(10,8,6) == 240` helps to understand how the function should work. 

For example, if the base is 10, the height is 8, and the width is 6, the function should return 240, which is the correct volume of the triangular prism. 