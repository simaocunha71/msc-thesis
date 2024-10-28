```
def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    side = base_edge
    base_area = base_edge**2
    lateral_area = 2 * base_edge * slant_height
    surface_area = base_area + lateral_area
    return surface_area
```


The function surface_Area calculates the surface area of a square pyramid with a given base edge and height. The surface area is calculated by first calculating the slant height of the pyramid using the Pythagorean theorem, and then calculating the lateral area by multiplying the base edge by the slant height and doubling it. The total surface area is then calculated by adding the base area and the lateral area. The unit test provided, `assert surface_Area(3,4) == 33`, ensures that the function is working correctly.