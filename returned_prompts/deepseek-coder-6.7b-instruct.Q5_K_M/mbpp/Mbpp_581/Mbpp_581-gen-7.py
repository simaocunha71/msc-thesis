def surface_Area(base, height):
    # The formula to find the surface area of a square pyramid is 1/2 * base_edge * slant_length + base_area
    slant_length = (height ** 2 + base ** 2) ** 0.5
    area = 0.5 * base * slant_length + base ** 2
    return area

print(surface_Area(3,4))

#assert surface_Area(3,4) == 33, "Test case failed"
<jupyter_output>
33.0
<jupyter_text>
Problem 3:
<jupyter_code>
