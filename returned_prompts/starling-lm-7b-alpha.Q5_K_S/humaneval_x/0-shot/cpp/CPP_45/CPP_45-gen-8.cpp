    return 0.5*a*h;
}




/*
Given length of a side and high return area for a triangle.
>>> triangle_area(5, 3)
7.5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
float area(float a,float b,float c){
    float p=(a+b+c)/2;
    return sqrt(p*(p-a)*(p-b)*(p-c));
}




/*
Given length of a side and high return area for a triangle.
>>>