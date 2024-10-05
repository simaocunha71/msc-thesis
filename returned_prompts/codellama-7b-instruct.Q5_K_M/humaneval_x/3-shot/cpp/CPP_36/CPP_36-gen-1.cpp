    int count=0;
    for (int i=11;i<n;i++)
    {
        int j=i;
        while (j%11==0)
        {
            count+=1;
            j/=11;
        }
        while (j%13==0)
        {
            count+=1;
            j/=13;
        }
    }
    return count;
}


