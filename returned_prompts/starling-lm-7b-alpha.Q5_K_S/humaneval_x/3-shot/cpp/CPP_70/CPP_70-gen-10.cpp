    vector<int> res;
    while (lst.size())
    {
        int min_val=*min_element(lst.begin(),lst.end());
        res.push_back(min_val);
        lst.erase(remove(lst.begin(),lst.end(),min_val),lst.end());
    }
    return res;
}



