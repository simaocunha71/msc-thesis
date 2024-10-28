    int i,j,k;
    int largest_even=0;
    for (i=x;i<=y;i++)
    {
        if (i%2==0)
        {
            if (i>largest_even)
            largest_even=i;
        }
    }
    if (largest_even==0)
    return -1;
    else
    return largest_even;
}




