    int count=0;
    for (int i=0;i<n.size();i++)
    {
        int sum=0,sign=1;
        if (n[i]<0)
        {
            sign=-1;
            n[i]=-n[i];
        }
        while (n[i]>0)
        {
            sum+=n[i]%10;
            n[i]/=10;
        }
        sum*=sign;
        if (sum>0)
        count++;
    }
    return count;
}