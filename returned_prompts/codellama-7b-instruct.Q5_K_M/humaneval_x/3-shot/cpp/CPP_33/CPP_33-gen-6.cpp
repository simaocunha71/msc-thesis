    vector<int> result;
    vector<int>::iterator it;
    for (it=l.begin();it!=l.end();it++)
    {
        if (*it%3==0)
        result.push_back(*it);
    }
    sort(result.begin(), result.end());
    for (it=l.begin();it!=l.end();it++)
    {
        if (*it%3!=0)
        result.push_back(*it);
    }
    return result;
}



