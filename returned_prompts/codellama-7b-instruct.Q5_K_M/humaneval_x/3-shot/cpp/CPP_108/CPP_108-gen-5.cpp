    int i;
    int c=0;
    int sum;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        while (n[i]>0)
        {
            sum+=n[i]%10;
            n[i]/=10;
        }
        if (sum>0)
        c+=1;
    }
    return c;
}



