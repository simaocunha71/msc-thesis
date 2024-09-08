Here is a simple program that fulfills your requirements. This program checks if the number `n` is a prime number. If it is, the function returns `x`, otherwise, it returns `y`.

```c
#include <stdio.h>
using namespace std;

int x_or_y(int n,int x,int y){
    if(n<2) return y;
    for(int i=2;i*i<=n;i++){
        if(n%i==0) return y;
    }
    return x;
}

int main()
{
    int n,x,y;
    printf("Enter the number n: ");
    scanf("%d",&n);
    printf("Enter the number x: ");
    scanf("%d",&x);
    printf("Enter the number y: ");
    scanf("%d",&y);
    printf("The output is: %d",x_or_y(n,x,y));
    return 0;
}
```

In this code, the `x_or_y` function checks if the number `n` is less than 2. If it is, the function returns `y`. If `n` is greater than or equal to 2, the function checks if `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, the function returns `y`. If `n` is not divisible by any of these numbers, the function returns `x`. The `main` function asks the user to input the values of `n`, `x`, and `y`, and then calls the `x_or_y` function with these values. The result is then printed to the console.