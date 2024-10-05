    if(a==0 || b==0 || c==0){
        return false;
    }
    float p = (a*a+b*b+c*c);
    float q = (a*a+b*b-c*c);
    float r = (a*a-b*b+c*c);
    float s = (a*a-b*b-c*c);
    float t = (a*a+b*b+c*c);
    if(p == 0 || q == 0 || r == 0 || s == 0 || t == 0){
        return false;
    }
    if(q/p == 1 || r/s == 1 || t/p == 1){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    printf("%d",right_angle_triangle(a,b,c));
    return 0;
}


Ans:
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
    if(a==0 || b==0 || c==0){
        return false;
    }
    if(a*a+b*b==c*c || a*a-b*b==c*c || a*a+b*b==c*c || a*a-b*b==c*c){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    float a,b,c;
    scanf