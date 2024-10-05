    vector<float> lp;
    vector<float> le;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        lp.push_back(l[i]);
        else
        le.push_back(l[i]);
    }
    sort(le.begin(), le.end());
    for (int i=0;i<le.size();i++)
    lp.push_back(le[i]);
    return lp;
}




