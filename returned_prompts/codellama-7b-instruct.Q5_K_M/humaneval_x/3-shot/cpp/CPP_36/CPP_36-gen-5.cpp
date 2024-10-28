    int count=0;
    int i=1;
    while (i<n)
    {
        if ((i%11==0) || (i%13==0))
        {
            if (i%10==7)
            count++;
        }
        i++;
    }
    return count;
}


