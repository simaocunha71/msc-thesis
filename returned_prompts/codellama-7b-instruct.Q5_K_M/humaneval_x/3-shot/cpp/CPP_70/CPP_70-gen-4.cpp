    vector<int> sorted;
    int i;
    int min_value=lst[0];
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<min_value)
            min_value=lst[i];
    }
    sorted.push_back(min_value);
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]==min_value)
            continue;
        int max_value=lst[i];
        for (int j=i+1;j<lst.size();j++)
        {
            if (lst[j]>max_value)
                max_value=lst[j];
        }
        sorted.push_back(max_value);
    }
    return sorted;
}


