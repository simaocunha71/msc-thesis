    int result=1;
    while (n>0)
    {
        if (n%2==1) result=(result*p)%1000000007;
        p=(p*p)%1000000007;
        n/=2;
    }
    return result;
}


