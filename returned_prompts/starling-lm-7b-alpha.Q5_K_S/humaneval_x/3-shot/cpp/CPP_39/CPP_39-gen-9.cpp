    int i,fib=0,prev_fib=0,next_fib=1,prime_fib=0;
    if (n==1)
    return 2;
    if (n==2)
    return 3;

    for (i=3;i<=n;i++)
    {
        fib=prev_fib+next_fib;
        prev_fib=next_fib;
        next_fib=fib;
        if (fib%2!=0 && fib>3){
        for (int j=3;j<=sqrt(fib);j++)
        if (fib%j==0)
        goto end_loop;
        prime_fib=fib;
        goto end_function;
        end_loop:;
        }
    }
    end_function:;
    return prime_fib;
}



