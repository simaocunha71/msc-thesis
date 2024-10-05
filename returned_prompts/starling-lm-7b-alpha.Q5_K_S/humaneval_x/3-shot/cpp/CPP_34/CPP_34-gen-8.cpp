    sort(l.begin(), l.end());
    vector<int> res;
    int i,j;
    int prev=-1;
    for (i=0;i<l.size();i++)
    {
        if (l[i]!=prev)
        {
        res.push_back(l[i]);
        prev=l[i];
        }
    }
    return res;
}




