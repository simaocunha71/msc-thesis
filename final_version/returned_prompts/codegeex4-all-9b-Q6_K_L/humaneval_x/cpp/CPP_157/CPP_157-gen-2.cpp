/*
Write a program to check whether a triangle is valid or not, if valid then print
the area of the triangle.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool right_angle_triangle(float a,float b,float c){
    float s=(a+b+c)/2;
    float area=sqrt(s*(s-a)*(s-b)*(s-c));
    printf("%f\n",area);
    return true;
}
int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    if(a+b>c && a+c>b && b+c>a){
        right_angle_triangle(a,b,c);
    }
    else{
        printf("not valid triangle\n");
    }
}