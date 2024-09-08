
The provided code calculates the area of a triangle given the length of a side and the height of the triangle. The formula used is (0.5)*a*h, where a is the length of the side and h is the height of the triangle.

Here is the corrected code:

```cpp
#include<stdio.h>
#include<math.h>
using namespace std;

float triangle_area(float a,float h){
    float area=(0.5)*a*h;
    return area;
}

int main()
{
    float a,h;
    printf("Enter the length of a side:");
    scanf("%f",&a);
    printf("Enter the high:");
    scanf("%f",&h);
    printf("Area of triangle is %f",triangle_area(a,h));
    return 0;
}
```

This code will correctly calculate and print the area of the triangle given the length of a side and the height. The area is calculated using the formula (0.5)*a*h, where a is the length of the side and h is the height of the triangle. The calculated area is then printed to the console. The user is prompted to enter the length of the side and the height, which are used as inputs to the function triangle_area(). The function returns the calculated area, which is then printed to the console.