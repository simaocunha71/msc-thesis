    int count=0;
    int i;
    for (i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            int j=i;
            while (j>0)
            {
                if (j%10==7)
                {
                    count+=1;
                }
                j/=10;
            }
        }
    }
    return count;
}