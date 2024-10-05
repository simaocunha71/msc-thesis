    int i,j;
    int frequency;
    int max_frequency=0;
    int max_value=-1;
    for (i=0;i<lst.size();i++)
    {
        frequency=0;
        for (j=0;j<lst.size();j++)
        if (lst[i]==lst[j])
        frequency+=1;
        if (frequency>=lst[i] && frequency>max_frequency)
        {
            max_frequency=frequency;
            max_value=lst[i];
        }
    }
    return max_value;
}

