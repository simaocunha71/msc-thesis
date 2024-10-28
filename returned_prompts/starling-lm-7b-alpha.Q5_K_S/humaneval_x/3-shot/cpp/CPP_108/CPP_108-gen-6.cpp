    int i,j,s,count=0;
    for (i=0;i<n.size();i++)
    {
        s=0;
        for (j=0;j<abs(n[i]);j++)
        {
            s+=abs(n[i])%10;
            n[i]/=10;
        }
        if (s>0) count+=1;
    }
    return count;
}



