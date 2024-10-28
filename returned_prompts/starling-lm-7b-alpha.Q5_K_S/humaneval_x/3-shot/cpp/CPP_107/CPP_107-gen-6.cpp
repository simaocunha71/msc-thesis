    int even=0, odd=0;
    int i;
    for (i=1;i<=n;i++)
    {
        string str=to_string(i);
        if (str==string(str.rbegin(),str.rend()))
        {
        if (i%2==0) even+=1;
        else odd+=1;
        }
    }
    vector<int> ans;
    ans.push_back(even);
    ans.push_back(odd);
    return ans;
}


