    vector<int> v;
    int i,j;
    for (i=0;i<l.size();i++)
    {
        v.push_back(l[i]);
    }
    sort(v.begin(),v.end());
    v.erase(unique(v.begin(),v.end()),v.end());
    return v;
}



