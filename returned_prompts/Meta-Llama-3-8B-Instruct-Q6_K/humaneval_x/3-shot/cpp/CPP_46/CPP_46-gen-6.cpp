    int f0=0;
    int f1=0;
    int f2=2;
    int f3=0;
    int result;
    for (int i=4;i<=n;i++)
    {
        result=f0+f1+f2+f3;
        f0=f1;
        f1=f2;
        f2=f3;
        f3=result;
    }
    return result;
}  // 1 ms


