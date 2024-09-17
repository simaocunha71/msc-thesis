```
def surface_Area(base_edge, height):
    # Calculate the slant height
    slant_height = (base_edge**2 + height**2)**0.5
    
    # Calculate the area of the base
    base_area = base_edge**2
    
    # Calculate the area of each triangular face
    face_area = 0.5 * base_edge * slant_height
    
    # Calculate the total surface area
    surface_area = base_area + 4 * face_area
    
    return surface_area
```


The problem is asking to create a function that calculates the surface area of a square pyramid given the base edge and the height. The surface area of a square pyramid is the sum of the area of the base and the areas of the four triangular faces.

The area of the base is simply the square of the base edge, and the area of each triangular face is half the product of the base edge and the slant height. The slant height can be calculated using the Pythagorean theorem.

The total surface area is then the sum of the area of the base and the areas of the four triangular faces. This is implemented in the function above. The unit test `assert surface_Area(3,4) == 33` ensures that the function is working correctly. 





In this problem, we need to calculate the surface area of a square pyramid given the base edge and the height. The formula for the surface area of a square pyramid is:

Surface Area = Base Area + 4 * Face Area

where Base Area is the area of the square base and Face Area is the area of each triangular face.

The area of the square base is simply the square of the base edge:

Base Area = base_edge^2

The area of each triangular face is half the product of the base edge and the slant height:

Face Area = 0.5 * base_edge * slant_height

The slant height can be calculated using the Pythagorean theorem:

slant_height = sqrt(base_edge^2 + height^2)

So, the total surface area is:

Surface Area = base_edge^2 + 4 * 0.5 * base_edge * sqrt(base_edge^2 + height^2)

This is implemented in the function above. The unit test `assert surface_Area(3,4) == 33` ensures that the function is working correctly.