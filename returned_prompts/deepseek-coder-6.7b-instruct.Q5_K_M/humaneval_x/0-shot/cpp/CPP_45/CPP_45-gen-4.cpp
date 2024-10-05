return 0.5*a*h;

}

int main() {

    float side,height,area;
    printf("Enter the length of side of triangle: ");
    scanf("%f",&side);
    printf("Enter the height of triangle: ");
    scanf("%f",&height);

    area=triangle_area(side,height);

    printf("The area of triangle is: %.2f",area);

    return 0;
}

*/

#include<stdio.h>
float triangle_area(float a,float h){
return 0.5*a*h;
}

int main() {

    float side,height,area;
    printf("Enter the length of side of triangle: ");
    scanf("%f",&side);
    printf("Enter the height of triangle: ");
    scanf("%f",&height);

    area=triangle_area(side,height);

    printf("The area of triangle is: %.2f",area);

    return 0;
}

//C++ Program to calculate the area of a triangle given the base and height/