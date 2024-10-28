    if (n<=3) return 0;
    int a=0,b=2,c=0,d=0,e=0,f=0;
    while (n>6){
        e=a+b+c+d;
        f=b+c+d;
        a=b;
        b=c;
        c=d;
        d=e;
        n-=5;
    }
    if (n==4) return e;
    if (n==5) return f;
    return b;
}


