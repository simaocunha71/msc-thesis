    if(n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("%dth fibonacci number is: %d",n,fib(n));
    return 0;
}
```

It's important to understand that the time complexity of this algorithm is exponential, O(2^n). This is due to the fact that every function call branches into two new calls in the recursive calls.

## Dynamic Programming Solution

Here is the solution with dynamic programming. This solution uses an array to store the Fibonacci numbers and avoids the recomputation of the same subproblem.

```cpp
#include<stdio.h>
using namespace std;

int fib(int n){
    int f[n+1];
    f[0] = 0;
    f[1] = 1;
    for(int i=2; i<=n; i++)
        f[i] = f[i-1] + f[i-2];
    return f[n];
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("%dth fibonacci number is: %d",n,fib(n));
    return 0;
}
```

The time complexity of the above solution is O(n), which is a significant improvement over the exponential time complexity of the recursive solution.

## Space Optimized Solution

Here is the solution with space optimized dynamic programming. This solution avoids the use of extra space and keeps only the last two numbers in the series.

```cpp
#include<stdio.h>
using namespace std;

int fib(int n){
    int a = 0, b = 1, c;
    if(n == 0)
        return a;
    for(int i=2; i<=n; i++){
        c = a + b;
        a = b;
        b = c;
    }
    return b