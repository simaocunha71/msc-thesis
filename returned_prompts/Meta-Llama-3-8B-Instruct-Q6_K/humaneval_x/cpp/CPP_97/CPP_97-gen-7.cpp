You can use the modulus operator to get the last digit of the numbers. For example, `a % 10` will give you the last digit of `a`.

Here is the correct code:

```cpp
#include<stdio.h>
using namespace std;
int multiply(int a,int b){
    int x = a % 10;
    int y = b % 10;
    return x*y;
}
int main(){
    printf("%d",multiply(148,412));
    return 0;
}
```

This code will return the product of the unit digits of the two numbers. For example, if you call `multiply(148,412)`, it will return `8*2=16`. If you call `multiply(19,28)`, it will return `9*8=72`. If you call `multiply(2020,1851)`, it will return `0*1=0`. If you call `multiply(14,-15)`, it will return `4*(-5)=20`. 

The code works by taking the modulus of the input numbers with 10. This gives the last digit of the numbers. It then multiplies these last digits together and returns the result. 

The `using namespace std;` line is used to bring the standard library into scope, allowing us to use standard library functions and classes. The `#include<stdio.h>` line is used to include the standard input/output library, which provides functions for input/output operations. The `int main()` function is the entry point of the program, and the `return 0;` statement at the end of the function indicates that the program has completed successfully. 

The `printf` function is used to print the result of the `multiply` function to the console. The `%d` in the `printf` function is a format specifier that indicates that the next argument should be printed as a decimal integer. 

The `multiply` function takes two integers as arguments, calculates the product of their unit digits, and returns the result. The `a % 10` expression calculates the last digit of `a`, and the `b % 10` expression calculates the last digit of `b`. The `x*y` expression calculates the product of these last digits. 

This code is a simple