    int i,j,frequency,max_frequency,max_value,value;
    max_frequency=-1;
    max_value=-1;
    for (i=0;i<lst.size();i++)
    {
        value=lst[i];
        frequency=0;
        for (j=0;j<lst.size();j++)
        if (lst[j]==value)
        frequency++;
        if (frequency>value && frequency>max_frequency)
        {
        max_frequency=frequency;
        max_value=value;
        }
    }
    if (max_frequency==-1)
    return -1;
    else
    return max_value;
}



