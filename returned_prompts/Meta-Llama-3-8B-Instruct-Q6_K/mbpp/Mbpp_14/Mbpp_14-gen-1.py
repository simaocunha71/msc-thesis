The problem is asking to write a function that calculates the volume of a triangular prism. The volume of a triangular prism can be calculated using the formula: (base_area * height) / 3, where base_area is the area of the triangle and height is the height of the prism.

From the given unit test `assert find_Volume(10,8,6) == 240`, we can understand that the function should take three parameters: base length, base width, and height. 

Here is the python function to solve the problem:

```Python
def find_Volume(base_length, base_width, height):
    base_area = 0.5 * base_length * base_width
    volume = (base_area * height) / 3
    return volume
```


This function first calculates the area of the triangle base using the formula (base_length * base_width) / 2. Then, it calculates the volume of the triangular prism by multiplying the base area with the height and dividing the result by 3. The function returns the calculated volume. 