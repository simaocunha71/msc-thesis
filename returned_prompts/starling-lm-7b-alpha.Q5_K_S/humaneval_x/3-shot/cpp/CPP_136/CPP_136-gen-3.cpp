    int i;
    int max_neg=-2147483648;
    int min_pos=2147483647;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0 && lst[i]>max_neg)
        {
        max_neg=lst[i];
        }
        if (lst[i]>0 && lst[i]<min_pos)
        {
        min_pos=lst[i];
        }
    }
    vector<int> result;
    result.push_back(max_neg);
    result.push_back(min_pos);
    return result;
}

