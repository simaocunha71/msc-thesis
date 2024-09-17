```
def surface_Area(base_edge, height):
    slant_height = (base_edge**2 + height**2)**0.5
    base_area = base_edge**2
    lateral_area = base_edge * slant_height * 4
    total_area = base_area + lateral_area
    return total_area
``` 
The function calculates the surface area of a square pyramid by first calculating the slant height, then the area of the base, and finally the lateral area. The base area is the square of the base edge, the lateral area is the product of the base edge, the slant height, and 4 (since there are four triangular faces on a square pyramid). The total area is the sum of the base area and the lateral area. The unit test `assert surface_Area(3,4) == 33` is used to verify the function's correctness. 





The surface area of a square pyramid is given by the formula:

A = base_area + lateral_area

The base area is the area of the square base, which is:

base_area = base_edge^2

The lateral area is the sum of the areas of the four triangular faces, which is:

lateral_area = 4 * (base_edge * slant_height)

The slant height is the distance from the apex to the edge of the base, which is:

slant_height = sqrt(base_edge^2 + height^2)

So the total surface area is:

A = base_edge^2 + 4 * (base_edge * sqrt(base_edge^2 + height^2))

The function takes two arguments, the base edge and the height, and returns the surface area. It uses the formula above to calculate the surface area.

The unit test `assert surface_Area(3,4) == 33` checks that the function returns the correct surface area for a square pyramid with a base edge of 3 and a height of 4. The expected output is 33.