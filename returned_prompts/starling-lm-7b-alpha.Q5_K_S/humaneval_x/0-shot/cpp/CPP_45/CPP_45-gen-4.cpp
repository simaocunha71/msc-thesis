    float s = (a + b + c) / 2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return area;
}



/*
Given length of a side and the included angle return the area.
>>> triangle_area_by_side_and_angle(3,75)
3.75
*/
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area_by_side_and_angle(float a,float angle){