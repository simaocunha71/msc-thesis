	if(a+b>c && a+c>b && b+c>a)
		return (a+b+c)/2;
	else
		return -1;
}
int main(){
	float a,b,c;
	scanf("%f %f %f",&a,&b,&c);
	float area = triangle_area(a,b,c);
	printf("%.2f",area);
}
Ans:
/*
Given the lengths of the three sides of a triangle. Return the area of the 
triangle rounded to 2 decimal points if the three sides form a valid triangle. 
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

	if(a+b>c && a+c>b && b+c>a){
		return (a+b+c)/2;
	}
	else{
		return -1;
	}
}
int main(){
	float a,b,c;
	scanf("%f %f %f",&a,&b,&c);
	float area = triangle_area(a,b,c);
	printf("%.2f",area);
}

