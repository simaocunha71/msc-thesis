    return x + y;
}
int main()
{
    int a,b;
    printf("Enter first number:");
    scanf("%d",&a);
    printf("Enter second number:");
    scanf("%d",&b);
    printf("Sum of the two numbers is: %d\n",add(a,b));
    return 0;
}

Solution:
The solution is to define a function named "add" which takes two integer arguments, adds them together, and returns the result. The function is then called in the main function with user inputted numbers.

Here is the corrected code:
```c
#include<stdio.h>
using namespace std;

int add(int x,int y){
    return x + y;
}

int main()
{
    int a,b;
    printf("Enter first number:");
    scanf("%d",&a);
    printf("Enter second number:");
    scanf("%d",&b);
    printf("Sum of the two numbers is: %d\n",add(a,b));
    return 0;
}
```
This code will correctly add two numbers entered by the user and display the result. The "add" function is a simple function that takes two integers, adds them together, and returns the result. In the main function, the user is prompted to enter two numbers, which are then passed to the "add" function and the result is displayed.