Explanation:
1. We check if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If it's not, we return -1.
2. We calculate the semi-perimeter `s` of the triangle using the formula `(a + b + c) / 2`.
3. We calculate the area of the triangle using Heron's formula: `area = sqrt(s*(s-a)*(s-b)*(s-c))`.
4. We round the area to 2 decimal points using `math.Round` and dividing by 100.

This solution correctly calculates the area of a triangle given its sides, and returns -1 if the sides do not form a valid triangle. It also rounds the area to 2 decimal points as required.