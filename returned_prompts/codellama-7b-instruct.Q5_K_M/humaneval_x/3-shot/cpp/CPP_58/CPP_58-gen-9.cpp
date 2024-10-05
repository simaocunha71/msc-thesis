    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator it;
    for (it=l1.begin();it!=l1.end();it++)
    {
        if (find(l2.begin(),l2.end(),*it)!=l2.end())
        result.push_back(*it);
    }
    sort(result.begin(),result.end());
    return result;
}


