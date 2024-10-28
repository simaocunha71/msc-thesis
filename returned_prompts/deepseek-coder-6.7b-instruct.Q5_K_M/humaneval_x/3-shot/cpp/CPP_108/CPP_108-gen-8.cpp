    int count=0;
    for(int i=0;i<n.size();i++)
    {
        int sum=0;
        if(n[i]<0)
        {
            sum+=n[i]%10;
            n[i]=n[i]/10;
        }
        while(n[i]>0)
        {
            sum+=n[i]%10;
            n[i]=n[i]/10;
        }
        if(sum>0)
        count++;
    }
    return count;
}

