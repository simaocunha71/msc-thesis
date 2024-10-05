    int a,b,c,d,e;
    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 2;
    if (n==3) return 0;
    a=fib4(n-1);
    b=fib4(n-2);
    c=fib4(n-3);
    d=fib4(n-4);
    return a+b+c+d;
}


