    vector<int> v=l;
    sort(v.begin(),v.end());
    vector<int>::iterator it;
    for (it=v.begin();it!=v.end();it++)
    {
        if (it!=v.begin() && *it==*(it-1))
            v.erase(it);
    }
    return v;
}  // or simply return unique(v.begin(), v.end()); from <algorithm> header


