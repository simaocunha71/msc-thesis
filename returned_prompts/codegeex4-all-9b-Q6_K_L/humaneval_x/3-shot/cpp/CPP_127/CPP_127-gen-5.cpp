    int a1=interval1[0],b1=interval1[1],a2=interval2[0],b2=interval2[1];
    int a,b;
    if (a1<=a2)
    a=a2;
    else
    a=a1;
    if (b1>=b2)
    b=b1;
    else
    b=b2;

    int len=b-a+1;
    if (len==1)
    return "NO";

    for (int i=2;i<len;i++)
    if (len%i==0)
    return "NO";

    return "YES";
}

