    sort(lst.begin(), lst.end());
    vector<int> result;
    while(!lst.empty()){
        result.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            result.push_back(lst.back());
            lst.pop_back();
        }
    }
    return result;
}


