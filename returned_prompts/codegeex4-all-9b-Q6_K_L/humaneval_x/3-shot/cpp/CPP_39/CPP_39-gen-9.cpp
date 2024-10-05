    int i=1;
    int a=2;
    int b=3;
    int temp;
    while (i<n)
    {
        temp=a;
        a=b;
        b=temp+a;
        i+=1;
    }
    return b;
}

