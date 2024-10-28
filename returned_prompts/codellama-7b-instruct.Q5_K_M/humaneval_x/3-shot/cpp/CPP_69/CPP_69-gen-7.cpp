    int i;
    int current_max=0;
    int current_max_count=0;
    int count;
    for (i=0;i<lst.size();i++)
    {
        count=0;
        for (j=0;j<lst.size();j++)
        {
            if (lst[i]==lst[j])
            count+=1;
        }
        if (count>=current_max_count)
        {
            if (count>current_max_count)
            {
                current_max_count=count;
                current_max=lst[i];
            }
        }
    }
    if (current_max_count>=current_max)
    return current_max;
    else
    return -1;
}


