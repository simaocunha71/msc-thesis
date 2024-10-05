    int count=0;
    for (int i=11;i<n;i++)
    {
        if (i%11==0 || i%13==0)
        {
            int k=i;
            while (k>0)
            {
                if (k%10==7)
                {
                    count+=1;
                }
                k=k/10;
            }
        }
    }
    for (int i=13;i<n;i++)
    {
        if (i%11==0 || i%13==0)
        {
            int k=i;
            while (k>0)
            {
                if (k%10==7)
                {
                    count+=1;
                }
                k=k/10;
            }
        }
    }
    return count;
}

