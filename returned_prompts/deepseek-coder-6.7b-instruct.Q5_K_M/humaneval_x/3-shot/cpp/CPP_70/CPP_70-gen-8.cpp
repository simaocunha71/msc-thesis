    sort(lst.begin(), lst.end());
    vector<int> res;
    while(!lst.empty()) {
        res.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()) {
            res.push_back(lst.back());
            lst.pop_back();
        }
    }
    return res;
}

