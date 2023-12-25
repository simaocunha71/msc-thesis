/*
Given the lengths of the three sides of a triangle. Return true if the three
sides form a right-angled triangle, false otherwise.
A right-angled triangle is a triangle in which one angle is right angle or 
90 degree.
Example:
right_angle_triangle(3, 4, 5) == true
right_angle_triangle(1, 2, 3) == false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool right_angle_triangle(float a,float b,float c){
    if(a==b && a!=c || a!=b&&b!=c && a!=c)  return false;
}
int main(){
	
	float a=0.0f,b=0.0f,c=0.0f;
	printf("Enter any of the side: \n");
	scanf("%d",&a);
	printf("Enter another side: \n");
	scanf("%d",&b);
	printf("Enter other side: \n");
	scanf("%d",&c);
	right_angle_triangle(a,b,c);
}
