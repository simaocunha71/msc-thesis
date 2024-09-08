}
F:
    if(lst.empty()){
        return {};
    }
    vector<int> res;
    sort(lst.begin(), lst.end());
    while(!lst.empty()){
        res.push_back(lst.back());
        lst.pop_back();
        if(!lst.empty()){
            res.push_back(lst.front());
            lst.erase(lst.begin());
        }
    }
    return res;
}

G:
    if(lst.empty()){
        return {};
    }
    vector<int> res;
    for(int i = 0; i < lst.size(); i++){
        res.push_back(*min_element(lst.begin() + i, lst.end()));
        lst.erase(remove(lst.begin() + i, lst.end(), *min_element(lst.begin() + i, lst.end())), lst.end());
        if(i < lst.size() - 1){
            res.push_back(*max_element(lst.begin(), lst.end()));
            lst.erase(remove(lst.begin(), lst.end(), *max_element(lst.begin(), lst.end())), lst