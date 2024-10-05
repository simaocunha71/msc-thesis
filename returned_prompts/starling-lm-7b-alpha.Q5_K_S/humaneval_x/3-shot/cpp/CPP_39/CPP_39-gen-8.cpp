    int fib_number=0,fib_num1=1,fib_num2=1,i;
    while (n>0)
    {
        fib_number=fib_num1+fib_num2;
        fib_num1=fib_num2;
        fib_num2=fib_number;
        if (fib_number>3 && is_prime(fib_number))
        return fib_number;
        n--;
    }
    return 0;
}


