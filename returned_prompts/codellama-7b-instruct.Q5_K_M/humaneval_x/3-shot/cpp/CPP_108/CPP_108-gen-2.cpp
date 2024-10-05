    int i,j,k,count=0;
    for (i=0;i<n.size();i++)
    {
        int sum=0;
        for (j=n[i];j>0;j=j/10)
        {
            k=j%10;
            sum+=k;
        }
        if (sum>0)
        count++;
    }
    return count;
}


