return 0.5*a*h;
}

int main(){
float a,h,area;
printf("Enter side and high of triangle: ");
scanf("%f%f",&a,&h);
area=triangle_area(a,h);
printf("Area of triangle is: %f",area);
return 0;
}

*/

#include<stdio.h>
float triangle_area(float a,float h){

return 0.5*a*h;
}

int main(){
float a,h,area;
printf("Enter side and high of triangle: ");
scanf("%f%f",&a,&h);
area=triangle_area(a,h);
printf("Area of triangle is: %f",area);
return 0;
}


// 