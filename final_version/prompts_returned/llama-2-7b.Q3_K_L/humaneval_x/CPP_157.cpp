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
    float diff=sqrt((a+b+c)*(a+b+c));
    if (diff== (a+b)||abs(a-b) == 180 || abs(a+b) == 360 ) return true;
    else {
        printf("Oops!!");
            return false;
    }
}
int main(){
    int n=3,l_tri[n];
    for (int i=0;i<n;i++) scanf("%d",&(l_tri[i]));
    right_angle_triangle(l_tri[0],l_tri[1],l_tri[2]);
}
