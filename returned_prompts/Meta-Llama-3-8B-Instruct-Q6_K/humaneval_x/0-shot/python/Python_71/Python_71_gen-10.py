
This function takes the lengths of the three sides of a triangle as input and returns the area of the triangle. It first checks if the three sides form a valid triangle by using the triangle inequality theorem, which states that the sum of any two sides must be greater than the third side. If the sides form a valid triangle, it calculates the area using Heron's formula, rounds the area to 2 decimal points, and returns it. If the sides do not form a valid triangle, it returns -1.

Here is how you can use this function:

```
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```

In the first example, the function returns the area of the triangle with sides 3, 4, and 5, which is 6.00. In the second example, the function returns -1 because the sides 1, 2, and 10 do not form a valid triangle.