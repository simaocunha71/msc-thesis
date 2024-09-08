    vector<int> result;
    if(lst.empty()) return result;
    sort(lst.begin(), lst.end());
    reverse(lst.begin(), lst.end());
    result.push_back(lst[0]);
    lst.erase(lst.begin());
    sort(lst.begin(), lst.end());
    reverse(lst.begin(), lst.end());
    while(!lst.empty()){
        result.push_back(lst[0]);
        lst.erase(lst.begin());
        if(!lst.empty()){
            sort(lst.begin(), lst.end());
            reverse(lst.begin(), lst.end());
        }
    }
    return result;
}