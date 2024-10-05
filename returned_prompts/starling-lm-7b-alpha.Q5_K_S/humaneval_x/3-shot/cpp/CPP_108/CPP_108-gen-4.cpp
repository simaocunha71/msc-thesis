    int i,sum=0;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        int abs_n=abs(n[i]);
        while (abs_n!=0)
        {
            sum+=abs_n%10;
            abs_n/=10;
        }
        if (sum>0)
        return 1;
    }
    return 0;
}




