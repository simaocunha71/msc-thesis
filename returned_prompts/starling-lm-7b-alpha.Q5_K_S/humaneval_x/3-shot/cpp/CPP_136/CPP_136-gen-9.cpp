    int i;
    int max=0;
    int min=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]>max)
        max=lst[i];
        if (lst[i]<0 && lst[i]<min)
        min=lst[i];
    }
    if (max<0 && min<0)
    return vector<int>{0,0};
    if (max>0 && min>0)
    return vector<int>{0,0};
    vector<int> ans;
    ans.push_back(max);
    ans.push_back(min);
    return ans;
}



