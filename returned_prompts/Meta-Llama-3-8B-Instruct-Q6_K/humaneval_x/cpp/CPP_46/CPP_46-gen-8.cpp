The problem is to efficiently compute the n-th element of the fib4 number sequence.  The given sequence is defined as follows:
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

To solve this problem, we can use a loop to calculate the n-th element.  The idea is to keep track of the last four elements of the sequence and use them to calculate the next element.

Here is the C++ code for the problem:

```cpp
#include<stdio.h>
using namespace std;
int fib4(int n){
    if(n<=3)
    {
        return n%2;
    }
    int a=0,b=0,c=0,d=2;
    for(int i=4; i<=n; i++)
    {
        int temp=a+b+c+d;
        a=b;c=d;
        d=temp%2;
    }
    return d;
}
int main(){
    printf("%d\n",fib4(5));
    printf("%d\n",fib4(6));
    printf("%d\n",fib4(7));
    return 0;
}
```

In this code, the function `fib4(int n)` calculates the n-th element of the fib4 sequence.  If `n` is less than or equal to 3, it returns `n%2`.  Otherwise, it initializes four variables `a`, `b`, `c`, and `d` to 0, 0, 0, and 2, respectively.  Then it enters a loop that runs from 4 to `n`.  In each iteration of the loop, it calculates the next element as the sum of the last four elements