    vector<int> l_sorted;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        l_sorted.push_back(l[i]);
        else
        l_sorted.push_back(l[i]);
    }
    sort(l_sorted.begin(),l_sorted.end());
    return l_sorted;
}


