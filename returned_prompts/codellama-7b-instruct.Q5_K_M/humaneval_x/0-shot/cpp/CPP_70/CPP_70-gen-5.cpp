    if (lst.size()<2)
        return lst;
    vector<int> res;
    sort(lst.begin(),lst.end());
    res.push_back(lst[0]);
    res.push_back(lst[lst.size()-1]);
    for (int i=1; i<lst.size()-1; i+=2)
        res.push_back(lst[i]);
    for (int i=0; i<lst.size()-1; i+=2)
        res.push_back(lst[i+1]);
    return res;
}
