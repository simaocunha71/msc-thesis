    vector<int> all_nums;
    vector<int> unique_common;
    int i;
    for (i=0;i<l1.size();i++)
    {
        if (find(l2.begin(),l2.end(),l1[i])!=l2.end())
        {
            if (find(all_nums.begin(),all_nums.end(),l1[i])==all_nums.end())
            {
                unique_common.push_back(l1[i]);
                all_nums.push_back(l1[i]);
            }
        }
    }
    return unique_common;
}


