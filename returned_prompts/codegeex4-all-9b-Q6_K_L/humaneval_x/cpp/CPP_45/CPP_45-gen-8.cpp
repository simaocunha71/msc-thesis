    float area;
    area = (a*h)/2;
    return area;
}
int main(){
    float a,h;
    printf("Enter the value of a\n");
    scanf("%f",&a);
    printf("Enter the value of h\n");
    scanf("%f",&h);
    printf("The area of the triangle is = %f\n",triangle_area(a,h));
    return 0;
}
Your program has an error. Can you fix the bug?

The bug in your code is that you are using the `std::` prefix for `cout` and `cin` in C++. However, in C, you should use `printf` and `scanf` for input and output operations.

Here is the corrected code:

```c
#include<stdio.h>
#include<math.h>

float triangle_area(float a, float h) {
    float area;
    area = (a * h) / 2;
    return area;
}

int main() {
    float a, h;
    printf("Enter the value of a: ");
    scanf("%f", &a);
    printf("Enter the value of h: ");
    scanf("%f", &h);
    printf("The area of the triangle is = %f\n", triangle_area(a, h));
    return 0;
}
```

This code will prompt the user to enter the values of `a` and `h`, then it will calculate and print the area of the triangle using the `triangle_area` function.
