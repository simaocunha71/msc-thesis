    vector<int> res;
    if(lst.empty()) return res;

    sort(lst.begin(), lst.end());
    res.push_back(lst[0]);
    lst.erase(lst.begin());

    sort(lst.begin(), lst.end(), greater<int>());
    res.push_back(lst[0]);
    lst.erase(lst.begin());

    while(!lst.empty()){
        sort(lst.begin(), lst.end());
        res.push_back(lst[0]);
        lst.erase(lst.begin());
        if(!lst.empty()){
            sort(lst.begin(), lst.end(), greater<int>());
            res.push_back(lst[0]);
            lst.erase(lst.begin());
        }
    }
    return res;
}