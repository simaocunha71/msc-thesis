    //Check if given sides form a valid triangle
    if(a + b <= c || b + c <= a || c + a <= b)
        return -1;

    //Calculate semi-perimeter
    float s = (a + b + c) / 2;

    //Calculate area using Heron's formula
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    //Return area rounded to 2 decimal points
    return round(area * 100) / 100;
}

int main() {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float res = triangle_area(a, b, c);
    if(res == -1) 
        printf("-1\n");
    else 
        printf("%.2f\n", res);
    return 0;
}

*/

#include <stdio.h>
#include <math.h>

float triangle_area(float a, float b, float c) {

    //Check if given sides form a valid triangle
    if(a + b <= c || b + c <= a || c + a <= b)
        return -1;

    //Calculate semi-perimeter
    float s = (a + b + c) / 2;

    //Calculate area using Heron's formula
    float area = sqrt(s * (s - a) * (s - b) * (s - c));

    //Return area rounded to 2 decimal points
    return round(area * 100) / 100;
}

int main() {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    float res = triangle_area(a, b, c);
    if(res == -1) 
        printf("-1\n");
    else 
        printf("%.2f\n", res);
    return 0;
}

//Q2:
/*
