    if(a+b>c && b+c>a && c+a>b){
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }
    else{
        return -1;
    }
}
int main(){
    float a,b,c;
    printf("Enter the sides of the triangle");
    scanf("%f %f %f",&a,&b,&c);
    float area=triangle_area(a,b,c);
    if(area==-1)
        printf("Invalid triangle sides");
    else
        printf("Area of triangle is %.2f",area);
    return 0;
}
*/


#include<stdio.h>
#include<math.h>
float triangle_area(float a,float b,float c){
    if(a+b>c && b+c>a && c+a>b){
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }
    else{
        return -1;
    }
}
int main(){
    float a,b,c;
    printf("Enter the sides of the triangle");
    scanf("%f %f %f",&a,&b,&c);
    float area=triangle_area(a,b,c);
    if(area==-1)
        printf("Invalid triangle sides");
    else
        printf("Area of triangle is %.2f",area);
    return 0;
}


// QUESTION ENDS
// CODE ENDS

//CODE STARTS
/*
