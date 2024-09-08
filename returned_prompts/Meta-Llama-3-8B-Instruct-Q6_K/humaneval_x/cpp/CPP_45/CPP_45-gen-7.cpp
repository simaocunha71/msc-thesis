    return 0.5*a*h;

}

int main()
{
    float a,h;
    printf("Enter the length of side:");
    scanf("%f",&a);
    printf("Enter the height:");
    scanf("%f",&h);
    printf("The area of triangle is: %f\n",triangle_area(a,h));
    return 0;
}

Answer:
The area of the triangle is calculated using the formula A = (b*h)/2, where 'b' is the base and 'h' is the height. In this code, the base 'b' is replaced by 'a', which is the length of the side. The function 'triangle_area' takes two parameters, 'a' and 'h', and returns the area of the triangle.

The code is written in C++ and uses the 'printf' function to print the result. The user is prompted to enter the length of the side and the height, and the result is printed to the console.

Here's the corrected code:

```c++
#include<stdio.h>
using namespace std;
float triangle_area(float a,float h){

    return 0.5*a*h;

}

int main()
{
    float a,h;
    printf("Enter the length of side:");
    scanf("%f",&a);
    printf("Enter the height:");
    scanf("%f",&h);
    printf("The area of triangle is: %f\n",triangle_area(a,h));
    return 0;
}
```

You can run this code and enter the values for 'a' and 'h' to get the area of the triangle. For example, if you enter '5' for 'a' and '3' for 'h', the output will be '7.5'.