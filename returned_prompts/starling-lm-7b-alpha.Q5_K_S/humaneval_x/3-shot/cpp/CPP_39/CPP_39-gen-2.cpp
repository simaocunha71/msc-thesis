    int i,fib_n,fib_n_minus_one,fib_n_minus_two;
    int prime_fib_n;
    fib_n=n;
    fib_n_minus_one=fib_n-1;
    fib_n_minus_two=fib_n_minus_one-1;
    while (true)
    {
        fib_n_minus_one/=2;
        fib_n_minus_two/=2;
        if (fib_n%fib_n_minus_one==0 && fib_n%fib_n_minus_two==0)
        {
            fib_n+=1;
        }
        else
        {
            prime_fib_n=fib_n;
            break;
        }
    }
    return prime_fib_n;
}



