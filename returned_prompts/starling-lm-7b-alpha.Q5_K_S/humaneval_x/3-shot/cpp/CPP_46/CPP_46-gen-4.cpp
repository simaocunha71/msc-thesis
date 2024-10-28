    int fib_4_n=0,fib_4_n_1=0,fib_4_n_2=0,fib_4_n_3=0;
    if (n==0)
    return 0;
    if (n==1)
    return 0;
    if (n==2)
    return 2;
    if (n==3)
    return 0;
    n-=4;
    fib_4_n_1=fib4(n-1);
    fib_4_n_2=fib4(n-2);
    fib_4_n_3=fib4(n-3);
    return fib_4_n_1+fib_4_n_2+fib_4_n_3;
}



