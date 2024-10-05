    int i,small,big;
    small=1000000000;
    big=-1000000000;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<small && lst[i]>0)
        {
            small=lst[i];
        }
        if (lst[i]>big && lst[i]<0)
        {
            big=lst[i];
        }
    }
    vector<int> ans;
    ans.push_back(big);
    ans.push_back(small);
    return ans;
}



