    if (n<2)
        return n;
    int a=0,b=1;
    int result;
    for (int i=2;i<n;i++)
    {
        result=a+b;
        a=b;
        b=result;
    }
    return result;
}
// or
int fib(int n){
    if (n<2)
        return n;
    return fib(n-1)+fib(n-2);
} // recursive version
// or
int fib(int n){
    double phi=(1+sqrt(5))/2;
    return (int)round(pow(phi,n)/sqrt(5));
} // using formula


