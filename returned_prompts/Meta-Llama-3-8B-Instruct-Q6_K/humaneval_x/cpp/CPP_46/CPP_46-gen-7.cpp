    int a[4] = {0,0,2,0};
    for(int i=4;i<=n;i++){
        int temp = a[0]+a[1]+a[2]+a[3];
        a[0] = a[1];
        a[1] = a[2];
        a[2] = a[3];
        a[3] = temp;
    }
    return a[n%4];
}

int main(){
    printf("%d\n",fib4(5));
    printf("%d\n",fib4(6));
    printf("%d\n",fib4(7));
    return 0;
}

B:
```c
#include <stdio.h>

int fib4(int n) {
    if (n <= 3) {
        return n == 0 || n == 1 ? 0 : 2;
    }

    int a = 0, b = 0, c = 2, d = 0;

    for (int i = 4; i <= n; i++) {
        int temp = a + b + c + d;
        d = c;
        c = b;
        b = a;
        a = temp;
    }

    return a;
}

int main() {
    printf("%d\n", fib4(5));
    printf("%d\n", fib4(6));
    printf("%d\n", fib4(7));
    return 0;
}
```

Explanation:
The problem is to write a function that efficiently computes the n-th element of the Fib4 number sequence. The Fib4 sequence is defined as follows:
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

The solution uses an iterative approach to compute the n-th element of the sequence. The idea is to store the last 4 elements of the sequence in an array and update them in each iteration. The array elements are updated as follows:
a[0] = a[1]
a[1] = a[2]
a[2] = a[3]
a[3] = a[0] + a[1] + a[2] + a[3]

The function takes an integer n as input and