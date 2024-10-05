    if (n<3)
        return 0;
    int a=0, b=0, c=1;
    for(int i=3;i<=n;i++)
    {
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
    }
    return c;
}
// or
int fibfib(int n){
    if(n<3) return 0;
    int a=0, b=0, c=1;
    for(int i=3;i<=n;i++)
        c=a+b+c, a=b, b=c;
    return c;
}
// or
int fibfib(int n){
    if(n<3) return 0;
    int a=0, b=0, c=0, d=0, e=1, f=1;
    for(int i=3;i<=n;i++)
        c=d+e+f, d=e, e=f, f=c;
    return f;
}