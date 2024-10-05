    vector<int> l2;
    vector<int>::iterator it;
    for (it=l.begin();it<l.end();it++)
    if (*it%3!=0)
    l2.push_back(*it);
    else
    l2.push_back(*it);

    sort(l2.begin(), l2.end());
    return l2;
}


