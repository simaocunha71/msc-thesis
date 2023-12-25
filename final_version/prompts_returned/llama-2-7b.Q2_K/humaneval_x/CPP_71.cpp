/*
Given the lengths of the three sides of a triangle. Return the area of
the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
Otherwise return -1
Three sides make a valid triangle when the sum of any two sides is greater 
than the third side.
Example:
triangle_area(3, 4, 5) == 6.00
triangle_area(1, 2, 10) == -1
*/
#include<stdio.h>
#include<math.h>
using namespace std;
float triangle_area(float a,float b,float c){
    float res=b+c;
    if(fabs(b-a)>fabs(res)){ //if the sum of the two sides is greater than 
        return -1;}
    else{return (res*0.5);}//the third side }
}
int main()
{
	int i,j;
	float ans=0,area=0;
	for(i=0;i<10;i++)  //taking input from user
	{	scanf("%d %d %d",&a, &b,&c); //scanning the three sides of triangle
		printf("Input: ");
		area=triangle_area(a,b,c);
		if(area>=0&&area!=1) 
		{ans+=area;}
	}return 0;
}