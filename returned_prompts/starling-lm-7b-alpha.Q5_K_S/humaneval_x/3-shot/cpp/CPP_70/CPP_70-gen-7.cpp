    vector<int> result;
    vector<int>::iterator min_it;
    vector<int>::iterator max_it;
    while (!lst.empty())
    {
        min_it=min_element(lst.begin(), lst.end());
        max_it=max_element(lst.begin(), lst.end());
        result.push_back(*min_it);
        lst.erase(min_it);
        result.push_back(*max_it);
        lst.erase(max_it);
    }
    return result;
}



