    vector<int> all_nums;
    vector<int> result;
    int i;
    for (i=0;i<x.size();i++)
    if (all_nums.size()==0)
    all_nums.push_back(x[i]);
    else
    {
        if (x[i]%2==1)
        {
        auto it=find(all_nums.begin(),all_nums.end(),x[i]);
        if (it==all_nums.end())
        {
        all_nums.push_back(x[i]);
        result.push_back(x[i]);
        }
        }
    }

    sort(result.begin(),result.end());
    return result;
}




