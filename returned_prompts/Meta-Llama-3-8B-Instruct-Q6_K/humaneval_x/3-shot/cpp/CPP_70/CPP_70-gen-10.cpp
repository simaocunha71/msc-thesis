    vector<int> result;
    while (!lst.empty()){
        int min_element = *min_element(lst.begin(), lst.end());
        result.push_back(min_element);
        lst.erase(remove(lst.begin(), lst.end(), min_element), lst.end());
        if (!lst.empty()){
            int max_element = *max_element(lst.begin(), lst.end());
            result.push_back(max_element);
            lst.erase(remove(lst.begin(), lst.end(), max_element), lst.end());
        }
    }
    return result;
}