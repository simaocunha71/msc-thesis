return (0.5)*a*h;

}
int main() {
float side,height;
printf("Enter the length of side and height of triangle: ");
scanf("%f %f",&side,&height);
printf("Area of the triangle is: %f",triangle_area(side,height));
return 0;
}
```

Output:
```bash
Enter the length of side and height of triangle: 5 3
Area of the triangle is: 7.500000
```

Explanation:
The program takes the length of the side and the height of a triangle as input from the user. It then calculates and prints the area of the triangle using the formula `(0.5)*base*height`.

The function `triangle_area(float a,float h)` calculates the area of the triangle and returns the result.

The function `main()` is the entry point of the program. It prints a message to the user asking for their input. It then calls the `triangle_area(float a,float h)` function with the user's input and prints the result.
*/

#include <stdio.h>

float triangle_area(float a, float h) {
    return (0.5) * a * h;
}

int main() {
    float side, height;
    printf("Enter the length of side and height of triangle: ");
    scanf("%f %f", &side, &height);
    printf("Area of the triangle is: %f\n", triangle_area(side, height));
    return 0;
}
```

This program will take in two inputs from the user: the length of a side of the triangle and the height of the triangle. It will then calculate the area of the triangle using the formula `(0.5) * base * height` and print the result.

For example, if the user inputs `5 3`, the program will print `Area of the triangle is: 7.500000`.
