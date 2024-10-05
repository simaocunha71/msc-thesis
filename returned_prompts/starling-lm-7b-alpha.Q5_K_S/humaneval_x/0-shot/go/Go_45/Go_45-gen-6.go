    return 0.5 * a * h
}

To find the area of a triangle, you can use the formula base × height ÷ 2. The TriangleArea function takes two arguments: the length of a side (a) and the height (h) of the triangle. It then returns the area of the triangle by multiplying the length of the side by the height and dividing the result by 2.

For example, if you call TriangleArea(5, 3), you'll get a result of 7.5, which is the area of the triangle with a side length of 5 and a height of 3.

The function uses the Heron's formula, which is a special case of the formula for the area of a triangle when the sides are in proportion to the square root of the semi-perimeter. In this case, since we're given the length of a side and the height, we can use a simpler formula to calculate the area.

To use the function, you can simply call it with the appropriate arguments. For example, TriangleArea(5, 3) will return the area of a triangle with a side length of 5 and a height of 3, which is 7.5.

Overall, the TriangleArea function provides a convenient way to calculate the area of a triangle based on the length of a side and the height of the triangle.

// Example usage:
TriangleArea(5, 3)

// Output:
7.5

// Explanation:
The TriangleArea function takes two arguments: the length of a side (a) and the height (h) of the triangle. It then returns the area of the triangle by multiplying the length of the side by the height and dividing the result by 2. In this case, with a side length of 5 and a height of 3, the area of the triangle is 7.5.

Here's a breakdown of the calculation:
- The area of a triangle is calculated by multiplying the base (side length) by the height and dividing by 2.
- In this example, the base is 5 and the height is 3, so the area is (5 * 3) ÷ 2 = 7.5.
- The TriangleArea function returns the calculated area, which is