    vector<int> sorted_list;
    int min_val=*min_element(lst.begin(), lst.end());
    sorted_list.push_back(min_val);
    lst.erase(find(lst.begin(), lst.end(), min_val));
    while (lst.size()>0)
    {
    min_val=*min_element(lst.begin(), lst.end());
    sorted_list.push_back(min_val);
    lst.erase(find(lst.begin(), lst.end(), min_val));
    }
    return sorted_list;
}


