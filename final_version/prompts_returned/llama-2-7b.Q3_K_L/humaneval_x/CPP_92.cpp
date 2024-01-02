/*
Create a function that takes 3 numbers.
Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
Returns false in any other cases.

Examples
any_int(5, 2, 7) ➞ true

any_int(3, 2, 2) ➞ false

any_int(3, -2, 1) ➞ true

any_int(3.6, -2.2, 2) ➞ false



*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){
	if((fabs(a-b)==0&&isnan(c))||(fabs(a-b)==0&&notnan(c))) return true;
	else if((fabs(a-c)==0&&isnan(b))||(fabs(a-c)==0&&notnan(b))) return true;
	else return false;
}
int main() {
    float x,y,z;
    scanf("%f%f%f",&x,&y,&z);
    bool b = any_int(x,y,z);
    if (b)  printf("true\n");
    else   printf("false\n");
}
