    int fib1=1,fib2=1,fib3,f=2;
    if(n==1) return 2;
    if(n==2) return 3;
    while(f<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        f++;
    }
    if(is_prime(fib3)) return fib3;
    else goto A;
}
B:
    int prime_fib(int n){

C:
    int fib1=1,fib2=1,fib3,f=2;
    if(n==1) return 2;
    if(n==2) return 3;
    while(f<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        f++;
    }
    if(is_prime(fib3)) return fib3;
    else goto B;
}
D:
    int prime_fib(int n){

E:
    int fib1=1,fib2=1,fib3,f=2;
    if(n==1) return 2;
    if(n==2) return 3;
    while(f<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        f++;
    }
    if(is_prime(fib3)) return fib3;
    else goto D;
}
F:
    int prime_fib(int n){

G:
    int fib1=1,fib2=1,fib3,f=2;
    if(n==1) return 2;
    if(n==2) return 3;
    while(f<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        f++;
    }
    if(is_prime(fib3)) return fib3;
    else goto F;
}
H:
    int prime_fib(int n){

I:
    int fib1=1,fib2=1,fib3,f=2;
    if(n==1) return 2;
    if(n==2) return 3;
    while(f<n)
    {
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
        f++;
    }
    if(is_prime(fib3)) return fib3;
    else goto H;
}
J:
    int