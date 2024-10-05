    vector<int> result;
    int min_val=lst[0];
    int max_val=lst[0];
    for (int i=1;i<lst.size();i++)
    {
        if (lst[i]<min_val)
        min_val=lst[i];
        if (lst[i]>max_val)
        max_val=lst[i];
    }

    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]==min_val)
        {
        result.push_back(min_val);
        for (int j=0;j<lst.size();j++)
        {
        if (lst[j]!=min_val && lst[j]!=max_val)
        {
        result.push_back(lst[j]);
        }
        }
        result.push_back(max_val);
        return result;
        }
    }
}


