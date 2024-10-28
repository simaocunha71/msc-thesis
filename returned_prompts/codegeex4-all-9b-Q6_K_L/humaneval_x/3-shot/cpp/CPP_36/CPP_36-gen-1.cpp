    int count=0;
    int i;
    for (i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            int temp=i;
            while (temp>0)
            {
            if (temp%10==7)
            count+=1;
            temp=temp/10;
            }
        }
    }
    return count;
}

