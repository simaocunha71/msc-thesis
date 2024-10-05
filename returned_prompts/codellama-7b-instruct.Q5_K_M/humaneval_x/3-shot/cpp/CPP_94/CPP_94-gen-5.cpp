    int largest=0, sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]>largest)
        {
            largest=lst[i];
        }
    }
    while (largest>0)
    {
        sum+=largest%10;
        largest/=10;
    }
    return sum;
}


