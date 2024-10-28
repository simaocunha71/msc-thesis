    long long result=1;
    int i;
    for (i=n;i>0;i--)
    {
        result*=(long long)i;
    }
    return result;
} // or return n*special_factorial(n-1); // recursive version


