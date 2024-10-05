    sort(l.begin(),l.end());
    vector<int> result;
    result.push_back(l[0]);
    int i;
    for (i=1;i<l.size();i++)
    if (l[i]!=l[i-1])
    result.push_back(l[i]);

    return result;
}



