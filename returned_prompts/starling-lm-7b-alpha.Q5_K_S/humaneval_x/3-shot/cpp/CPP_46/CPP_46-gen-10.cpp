    int fib1, fib2, fib3, fib4, i;
    fib1=0;
    fib2=0;
    fib3=2;
    fib4=0;
    if (n==0) return fib1;
    if (n==1) return fib2;
    if (n==2) return fib3;
    if (n==3) return fib4;
    for (i=4;i<n;i++)
    {
        fib4=fib1+fib2+fib3+fib4;
        fib1=fib2;
        fib2=fib3;
        fib3=fib4;
    }
    return fib4;
}


