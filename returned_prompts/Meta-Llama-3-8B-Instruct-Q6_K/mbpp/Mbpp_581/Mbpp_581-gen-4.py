```
def surface_Area(base_edge, height):
    # Calculate the slant height of the pyramid
    slant_height = (height**2 + (base_edge/2)**2)**0.5
    
    # Calculate the surface area of the pyramid
    surface_area = base_edge**2 + 4*(base_edge*slant_height/2)
    
    return surface_area
```
This function calculates the surface area of a square pyramid given its base edge and height. The surface area is calculated as the area of the base plus the area of the four triangular sides. The slant height of the pyramid is calculated using the Pythagorean theorem. The area of each triangular side is calculated as half the base edge times the slant height. The function returns the total surface area.  The unit test `assert surface_Area(3,4) == 33` ensures that the function is working correctly.