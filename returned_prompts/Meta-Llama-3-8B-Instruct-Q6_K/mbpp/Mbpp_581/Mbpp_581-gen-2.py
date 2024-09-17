```
def surface_Area(base_edge, height):
    side = base_edge
    slant_height = (side**2 + height**2)**0.5
    base_area = side**2
    lateral_area = 2 * base_area + 4 * side * slant_height
    return base_area + lateral_area
```



The surface area of a square pyramid can be calculated by summing up the areas of its base and its lateral surface. The area of the base is the square of the base edge, and the lateral surface area is 2 times the base area plus 4 times the product of the base edge and the slant height. The slant height is the square root of the sum of the squares of the base edge and the height.

The unit test `assert surface_Area(3,4) == 33` suggests that the function should return 33 when the base edge is 3 and the height is 4.

Here is a Python function that calculates the surface area of a square pyramid:

```python
def surface_Area(base_edge, height):
    side = base_edge
    slant_height = (side**2 + height**2)**0.5
    base_area = side**2
    lateral_area = 2 * base_area + 4 * side * slant_height
    return base_area + lateral_area
```

This function first calculates the side length and the slant height of the pyramid. Then it calculates the area of the base and the lateral surface area. Finally, it returns the sum of the base area and the lateral surface area.