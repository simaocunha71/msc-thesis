    int n=xs.size();
    int m=n/2;
    if (n%2!=0)
    {
        printf("Error: find_zero takes even number of coefficients.\n");
        return 0;
    }
    if (xs[m]==0)
    {
        printf("Error: find_zero takes coefficients with non zero largest coefficient.\n");
        return 0;
    }
    if (xs[m]>0)
    {
        for (int i=m-1;i>0;i--)
        {
            if (xs[i]!=0)
            {
                printf("Error: find_zero takes coefficients with non zero largest coefficient.\n");
                return 0;
            }
        }
    }
    else
    {
        for (int i=m-1;i>0;i--)
        {
            if (xs[i]==0)
            {
                printf("Error: find_zero takes coefficients with non zero largest coefficient.\n");
                return 0;
            }
        }
    }
    if (xs[m]>1)
    {
        for (int i=m-2;i>0;i--)
        {
            if (xs[i]!=0)
            {
                printf("Error: find_zero takes coefficients with non zero largest coefficient.\n");
                return 0;
            }
        }
    }
    else
    {
        for (int i=m-2;i>0;i--)
        {
            if (xs[i]==0)
            {
                printf("Error: find_zero takes coefficients with non zero largest coefficient.\n");
                return 0;
            }
        }
    }
    int i;
    double x_min=-1,x_max=1;
    double x_new=0;
    for (i=0;i<50;i++)
    {
        x_new=(x_min+x_max)/2;
        if (poly(xs,x_new)==0)
        {
            return x_new;
        }
        else if (poly(