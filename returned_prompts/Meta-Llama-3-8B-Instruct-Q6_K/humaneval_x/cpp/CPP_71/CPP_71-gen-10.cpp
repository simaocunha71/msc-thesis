float triangle_area(float a,float b,float c){
    if ((a + b > c) && (a + c > b) && (b + c > a))
    {
        float s = (a + b + c) / 2.0;
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return round(area * 100.0) / 100.0;
    }
    else
    {
        return -1.0;
    }
}
int main()
{
    printf("%f", triangle_area(3,4,5));
    return 0;
}
```
Output:
```
6.000000
```
This C++ program calculates the area of a triangle given the lengths of its sides. The function `triangle_area` takes three float parameters `a`, `b`, and `c` representing the lengths of the sides of the triangle. It first checks if the three sides form a valid triangle by verifying the triangle inequality. If the sides form a valid triangle, it calculates the area using Heron's formula. The area is then rounded to 2 decimal points and returned. If the sides do not form a valid triangle, it returns -1.0. In the `main` function, we test the function with the sides of a valid triangle (3, 4, 5) and print the result. The output is 6.000000, which is the area of the triangle rounded to 2 decimal points. If we test the function with sides that do not form a valid triangle, it will return -1.0.