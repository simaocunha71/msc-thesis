    int i,sum;
    int count=0;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        while (n[i]!=0)
        {
            sum+=n[i]%10;
            n[i]/=10;
        }
        if (sum>0)
        count++;
    }
    return count;
}



