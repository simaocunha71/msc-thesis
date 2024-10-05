if(a == (b+c) && a == (int)a && b == (int)b && c == (int)c){
return true;
}
else{
return false;
}
}

int main(){
float a,b,c;
printf("Enter three numbers:");
scanf("%f %f %f",&a,&b,&c);
if(any_int(a,b,c)==1){
printf("true");
}
else{
printf("false");
}
return 0;
}

Here,
I have created a function named any_int that takes three numbers as input and checks if one of the numbers is the sum of the other two, and all numbers are integers. If the condition is met, it returns true, otherwise it returns false.
In the main function, I have taken three inputs from the user and called the any_int function with these inputs. If the function returns true (1), I have printed "true" as output. If the function returns false (0), I have printed "false" as output.

A: The code you've written checks if the sum of two numbers is equal to the third number and all numbers are integer. However, there is a mistake in the line where you're checking the sum of two numbers.

You're checking if a is equal to b+c, but you're comparing a with the sum of b and c, not a with the result of the sum (b+c).

Here is the corrected code:
#include<stdio.h>
using namespace std;

bool any_int(int a, int b, int c){
    return ((a == b + c) && (a == (int)a) && (b == (int)b) && (c == (int)c));
}

int main(){
    int a,b,c;
    printf("Enter three numbers:");
    scanf("%d %d %d",&a,&b,&c);
    if(any_int(a,b,c)){
        printf("true");
    }
    else{
        printf("false");
    }
    return 0;
}

This version of the code should work as expected.

