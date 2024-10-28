    int max=0,frequency=0,i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>=max)
        {
            frequency=1;
            max=lst[i];
        }
        if (lst[i]==max)
        frequency+=1;
    }
    if (frequency>=max)
    return max;
    else
    return -1;
}


