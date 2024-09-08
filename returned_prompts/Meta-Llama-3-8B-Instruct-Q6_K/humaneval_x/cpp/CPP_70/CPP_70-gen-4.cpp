    vector<int> result;
    if(lst.empty()) return result;
    sort(lst.begin(), lst.end());
    for(int i = 0; i < lst.size(); i++){
        if(i % 2 == 0) result.push_back(lst[i]);
        else result.push_back(lst[lst.size() - 1 - i]);
    }
    return result;
}
