    int count=0;
    int i,j;
    int sum;
    for (i=0;i<n.size();i++)
    {
        if (n[i]<0)
        {
            sum=abs(n[i]);
            for (j=0;sum>0;j++)
            {
                sum=(sum-(sum%10))/10;
            }
            if (j>0)
            count+=1;
        }
        else
        {
            sum=n[i];
            for (j=0;sum>0;j++)
            {
                sum=(sum-(sum%10))/10;
            }
            if (j>0)
            count+=1;
        }
    }
    return count;
}

