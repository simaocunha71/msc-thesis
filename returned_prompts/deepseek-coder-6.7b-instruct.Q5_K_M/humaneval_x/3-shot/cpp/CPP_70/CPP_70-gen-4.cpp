    sort(lst.begin(), lst.end());
    vector<int> sorted;
    while (!lst.empty()) {
        sorted.push_back(lst.front());
        lst.erase(lst.begin());
        if (!lst.empty()) {
            sorted.push_back(lst.back());
            lst.pop_back();
        }
    }
    return sorted;
}


