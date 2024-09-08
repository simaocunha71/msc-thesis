if ((a+b>c)&&(a+c>b)&&(b+c>a)) {
    float s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return round(area*100.0)/100.0;
}
else return -1.0;
}
int main() {
    printf("%.2f",triangle_area(3,4,5));
    printf("\n");
    printf("%.2f",triangle_area(1,2,10));
    return 0;
}

R:
The code provided is a C++ program that calculates the area of a triangle given its sides. The formula used is Heron's formula, which is `sqrt(s*(s-a)*(s-b)*(s-c))`, where `s` is the semi-perimeter of the triangle.

Here is the breakdown of the code:

1. The `triangle_area` function takes three parameters `a`, `b`, and `c` representing the sides of the triangle.
2. The function checks if the three sides form a valid triangle by verifying if the sum of any two sides is greater than the third side. If this condition is not met, the function returns -1.
3. If the sides form a valid triangle, the function calculates the semi-perimeter `s` as `(a+b+c)/2`.
4. The area of the triangle is calculated using Heron's formula and is returned as a floating-point number.
5. The `main` function demonstrates the usage of the `triangle_area` function by calling it with two sets of side lengths and printing the results.

The output of the program will be:

6.00
-1.00

Note that the `round` function is used to round the area to 2 decimal points. The `100.0` in the `round` function is used to specify the number of decimal points to round to. The `round` function returns an integer, so the `/100.0` is used to convert the result back to a floating-point number.