#include<stdio.h>
#include<math.h>
using namespace std;
bool right_angle_triangle(float a,float b,float c){
    float d;
    if(a>b&&a>c){
    d=pow(a,2);
    }
    else if(b>a&&b>c){
    d=pow(b,2);
    }
    else{
    d=pow(c,2);
    }
    if(d==pow(a+b,2)||d==pow(a+c,2)||d==pow(b+c,2)){
    return true;
    }
    else{
    return false;
    }
}
