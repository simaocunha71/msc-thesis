    # First, let's check if the sides form a valid triangle
    def is_triangle(a, b, c):
        return (a + b > c) and (b + c > a) and (a + c > b)

    if not is_triangle(a, b, c):
        return -1

    # If the sides are valid, we can calculate the semi-perimeter
    s = (a + b + c) / 2

    # Then we can calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return round(area, 2)



# To test, uncomment and run the following line:
# print(triangle_area(3, 4, 5))


