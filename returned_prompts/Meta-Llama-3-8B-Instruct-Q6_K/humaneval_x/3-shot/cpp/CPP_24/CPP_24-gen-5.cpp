    for(int i=n-1;i>=1;i--)
    {
        if(n%i==0)
        {
            return i;
        }
    }
    return 1;
} // The largest divisor of 1 is 1 itself, so this function will return 1 in that case.