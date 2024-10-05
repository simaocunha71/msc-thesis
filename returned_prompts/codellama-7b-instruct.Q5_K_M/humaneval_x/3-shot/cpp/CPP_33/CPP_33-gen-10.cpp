    vector<int> lp;
    vector<int> lf;
    vector<int> lr;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%3==0)
        lp.push_back(l[i]);
        if (i%3==1)
        lf.push_back(l[i]);
        if (i%3==2)
        lr.push_back(l[i]);
    }
    sort(lp.begin(),lp.end());
    sort(lf.begin(),lf.end());
    sort(lr.begin(),lr.end());
    l.clear();
    l.insert(l.begin(),lp.begin(),lp.end());
    l.insert(l.end(),lf.begin(),lf.end());
    l.insert(l.end(),lr.begin(),lr.end());
    return l;
}

