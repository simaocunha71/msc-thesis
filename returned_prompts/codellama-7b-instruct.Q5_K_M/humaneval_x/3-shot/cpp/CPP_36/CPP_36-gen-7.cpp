    int count=0;
    int i;
    for (i=0;i<n;i++)
    {
        if (i%11==0 || i%13==0)
        count+=i%7==0;
    }
    return count;
}


