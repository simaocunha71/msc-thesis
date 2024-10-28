    int a=0, b=0, c=2, d=0;
    while (n>0){
        int temp=a;
        a=b;
        b=c;
        c=d;
        d=temp+a+b+c;
        n-=1;
    }
    return d;
}


