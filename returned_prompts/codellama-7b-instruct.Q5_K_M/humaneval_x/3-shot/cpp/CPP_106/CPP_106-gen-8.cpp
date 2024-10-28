    vector<int> ans;
    int i;
    for (i=1;i<=n;i++)
    {
        if (i%2==0)
        ans.push_back(i*f(i-1));
        else
        ans.push_back(f(i-1)+i);
    }
    return ans;
}



