    float sum=0;
    int i;
    for(i=0;i<lst.size();i++)
    {
        sum+=ceil(lst[i])*ceil(lst[i]);
    }
    return (int)sum;
}
