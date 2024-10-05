    sort(l.begin(),l.end());
    vector<int> r;
    int i;
    r.push_back(l[0]);
    for (i=1;i<l.size();i++)
    if (r.back()!=l[i])
    r.push_back(l[i]);
    return r;
}


