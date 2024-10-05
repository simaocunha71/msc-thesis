    int i,largest_factor=0;
    int sqrt_n=(int)sqrt(n);
    for (i=2;i<=sqrt_n;i++)
    {
        if (n%i==0)
        {
            if (i==n/i){
            largest_factor=i;
            }
            else
            {
            largest_factor=max(largest_factor,i,n/i);
            }
        }
    }
    return largest_factor;
}



