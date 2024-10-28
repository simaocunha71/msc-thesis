    if (n == 0){
        return 0;
    }
    if (n == 1){
        return 0;
    }
    if (n == 2){
        return 1;
    }
    int a = 0;
    int b = 0;
    int c = 1;
    int fib = 0;
    for (int i = 3; i <= n; i++){
        fib = a + b + c;
        a = b;
        b = c;
        c = fib;
    }
    return fib;
}
int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("%d-th fibfib number is: %d", n, fibfib(n));
    return 0;
}


A: This problem can be solved by using dynamic programming.
Here is the Python code for the function.
def fibfib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 0
    fib[2] = 1

    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
    return fib[n]

This code will return the n-th FibFib number.
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24

A: Here is the C++ solution:

```cpp
#include<iostream>
using namespace std;

int fibfib(int n) {
    if(n==0) return 0;
    if(n==1) return 0;
    if(n==2) return 1;

    int fib[n+1];
    fib[0] = 0;
    fib[1] = 0;
    fib[2] = 1;

    for(int i