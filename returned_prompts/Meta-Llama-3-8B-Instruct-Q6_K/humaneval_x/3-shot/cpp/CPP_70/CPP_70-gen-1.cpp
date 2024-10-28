    vector<int> result;
    sort(lst.begin(), lst.end());
    while (!lst.empty()) {
        result.push_back(lst.back());
        lst.pop_back();
        if (!lst.empty()) {
            sort(lst.begin(), lst.end());
            lst.pop_back();
        }
    }
    return result;
}


