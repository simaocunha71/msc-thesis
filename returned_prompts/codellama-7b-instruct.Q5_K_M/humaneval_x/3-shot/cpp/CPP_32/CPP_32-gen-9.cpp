    int n=xs.size();
    if (n%2!=0)
    printf("Error: odd number of coefficients");
    else
    {
        int largest_idx=0;
        for (int i=0;i<n;i++)
        {
            if (abs(xs[i])>abs(xs[largest_idx]))
            largest_idx=i;
        }
        int first_zero=0;
        if (xs[largest_idx]>0)
        {
        first_zero=(n-1)/2;
        }
        else
        {
        first_zero=n/2;
        }
        return -first_zero;
    }
}


