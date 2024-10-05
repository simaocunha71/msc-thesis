    if(a + b > c && a + c > b && b + c > a){
        float s = (a + b + c) / 2;
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return roundf(area * 100) / 100;
    }
    else{
        return -1;
    }
}

int main(){
    float a, b, c;
    printf("Enter the lengths of the three sides of the triangle:\n");
    scanf("%f%f%f", &a, &b, &c);
    float res = triangle_area(a, b, c);
    if(res != -1){
        printf("The area of the triangle is %.2f\n", res);
    }
    else{
        printf("The given sides do not form a valid triangle\n");
    }
    return 0;
}

*/

#include<stdio.h>
#include<math.h>
float triangle_area(float a,float b,float c){
    if(a + b > c && a + c > b && b + c > a){
        float s = (a + b + c) / 2;
        float area = sqrt(s * (s - a) * (s - b) * (s - c));
        return roundf(area * 100) / 100;
    }
    else{
        return -1;
    }
}

int main(){
    float a, b, c;
    printf("Enter the lengths of the three sides of the triangle:\n");
    scanf("%f%f%f", &a, &b, &c);
    float res = triangle_area(a, b, c);
    if(res != -1){
        printf("The area of the triangle is %.2f\n", res);
    }
    else{
        printf("The given sides do not form a valid triangle\n");
    }
    return 0;
}

//The given sides can form a triangle only if the sum of