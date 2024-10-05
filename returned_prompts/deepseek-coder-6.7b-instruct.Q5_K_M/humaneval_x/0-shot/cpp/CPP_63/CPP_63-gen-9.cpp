    if(n==0) return 0;
    if(n==1) return 0;
    if(n==2) return 1;

B:
    int fibfib_seq[n+1];
    fibfib_seq[0] = 0;
    fibfib_seq[1] = 0;
    fibfib_seq[2] = 1;

C:
    for(int i=3; i<=n; i++){
        fibfib_seq[i] = fibfib_seq[i-1] + fibfib_seq[i-2] + fibfib_seq[i-3];
    }

D:
    return fibfib_seq[n];
}

int main(){
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}
```

## Solution:
The solution provided is correct. However, for better performance, you can use a constant space approach with an algorithm that keeps track of only the last three numbers in the sequence. Here's an optimized version of the solution:

```cpp
#include<stdio.h>

int fibfib(int n){
    if(n==0) return 0;
    if(n==1) return 0;
    if(n==2) return 1;

    int fibfib_0 = 0, fibfib_1 = 0, fibfib_2 = 1;
    int fibfib_n;

    for(int i=3; i<=n; i++){
        fibfib_n = fibfib_0 + fibfib_1 + fibfib_2;
        fibfib_0 = fibfib_1;
        fibfib_1 = fibfib_2;
        fibfib_2 = fibfib_n;
    }

    return fibfib_2;
}

int main(){
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(