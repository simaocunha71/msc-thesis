    int max=-1000000000;
    int min=1000000000;
    int i;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        if (lst[i]>max)
        {
            max=lst[i];
        }
        if (lst[i]>0)
        if (lst[i]<min)
        {
            min=lst[i];
        }
    }
    vector<int> res;
    res.push_back(max);
    res.push_back(min);
    return res;
}



