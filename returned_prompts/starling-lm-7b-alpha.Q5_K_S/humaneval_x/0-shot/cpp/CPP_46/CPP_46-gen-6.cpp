    static int f[2][5];
    if(n==0||n==1)return 0;
    if(n==2)return 2;
    if(n==3)return 0;
    if(f[n%4][n/4]!=0)return f[n%4][n/4];
    f[n%4][n/4]=fib4(n-1)+fib4(n-2)+fib4(n-3)+fib4(n-4);
    return f[n%4][n/4];
}



int main(){
    printf("%d\n",fib4(5));
    printf("%d\n",fib4(6));
    printf("%d\n",fib4(7));
    return 0;
}





*/


/*
In the original problem, we need to compute the nth element of the fib4 number sequence.
The fib4 number sequence is defined as follows:

fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

To efficiently compute the nth element of the fib4 number sequence, we can use the following approach:

Define two arrays: f[0:4] and f[1:4]. Initialize f[0:4] with the first four elements of the fib4 number sequence. Initialize f[1:4] with the next four elements of the fib4 number sequence.

For each n from 5 to infinity, do the following steps:

1. Check whether f[n % 4][n / 4] is 0. If it is 0, it means that we haven't computed the nth element of the fib4 number sequence yet. In this case, we need to compute it and store it in f[n % 4][n / 4]. To compute the nth element, we can use the recurrence relation fib4(n) = fib4(n -