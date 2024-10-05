    int result=1;
    while (n>0)
    {
        if (n%2==1)
        result=(result*p)%100;
        p=(p*p)%100;
        n/=2;
    }
    return result;
}

