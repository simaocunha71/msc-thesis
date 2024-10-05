	if(a+b<=c){
		return -1;
	}
	else if(a==b&&b==c){
		return 0;
	}
	else{
		return (a*b)/2;
	}
}
int main(){
	float a,b,c;
	scanf("%f %f %f",&a,&b,&c);
	printf("%f",triangle_area(a,b,c));
	return 0;
}

Ans:
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
#include<stdio.h