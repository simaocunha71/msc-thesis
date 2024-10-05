    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());
    vector<int> all;
    vector<int>::iterator it;
    vector<int>::iterator it2;
    it=unique(l1.begin(), l1.end());
    it2=unique(l2.begin(), l2.end());
    for (it;it<l1.end();it++)
    {
        for (it2;it2<l2.end();it2++)
        if (*it==*it2)
        all.push_back(*it);
    }
    sort(all.begin(), all.end());
    return all;
}


