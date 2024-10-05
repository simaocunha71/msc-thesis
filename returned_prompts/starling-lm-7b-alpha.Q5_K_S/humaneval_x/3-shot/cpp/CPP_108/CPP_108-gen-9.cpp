    int i,count=0;
    int tmp;
    for (i=0;i<n.size();i++)
    {
        tmp=abs(n[i]);
        while (tmp>0)
        {
            if (tmp%10>0)
            count+=1;
            tmp/=10;
        }
    }
    return count;
}




