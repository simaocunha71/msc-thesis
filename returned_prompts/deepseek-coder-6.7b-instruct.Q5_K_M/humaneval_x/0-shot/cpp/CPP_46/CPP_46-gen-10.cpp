    if (n<0) return -1;
    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 2;
    if (n==3) return 0;

B:
    int fib3 = 0;
    int fib2 = 0;
    int fib1 = 2;
    int fib0 = 0;
    int fibn = 0;

C:
    for (int i=4; i<=n; i++){
        fibn = fib3 + fib2 + fib1 + fib0;
        fib3 = fib2;
        fib2 = fib1;
        fib1 = fib0;
        fib0 = fibn;
    }

D:
    return fibn;
}
int main()
{
    printf("fib4(5)=%d\n", fib4(5));
    printf("fib4(6)=%d\n", fib4(6));
    printf("fib4(7)=%d\n", fib4(7));
    return 0;
}
```

Answer:
The program provided here calculates the n-th element of the fib4 sequence by iterating from 4 to n and updating the values of the last four numbers in the sequence at each step. This is a dynamic programming approach that avoids recursion and has a time complexity of O(n). 

The program begins by initializing the first four terms of the sequence. Then it enters a loop that continues until the n-th term is calculated. Inside the loop, it calculates the n-th term as the sum of the last four terms and updates the last four terms to the new values. Finally, it returns the n-th term. 

The main function demonstrates the usage of the fib4 function by printing the fifth, sixth, and seventh terms of the sequence. The results match the expected outputs provided in the question.
