    if(n <= 1) return 0;
    else if(n == 2) return 1;
    else{
        int a = 0, b = 0, c = 1;
        for(int i = 3; i <= n; i++){
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
int main(){
    printf("%d\n",fibfib(5));
    return 0;
}

Answer:
Your code seems to be correct. It's a dynamic programming solution which calculates the nth term of the fibfib sequence. 

However, the function doesn't handle the case where n is less than 1. It would be a good idea to add a check at the beginning of the function to handle this case.

Here is the corrected code:

```c
#include<stdio.h>
using namespace std;
int fibfib(int n){
    if(n < 1) return -1; // return an error value if n is less than 1
    if(n <= 1) return 0;
    else if(n == 2) return 1;
    else{
        int a = 0, b = 0, c = 1;
        for(int i = 3; i <= n; i++){
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
int main(){
    printf("%d\n",fibfib(5));
    return 0;
}
```

In this code, if the input is less than 1, the function returns -1. This is a common practice in programming where you want to indicate an error. 

Also, note that fibfib(0) == 0 and fibfib(1) == 0 in the problem statement. So, the function is modified to return 0 for n <= 1. 

This code should work correctly for all positive integers n. For negative integers or non-integer values, it returns -1. 