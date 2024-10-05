    if (dict.size()==0)
    return false;
    string first_key=dict.begin()->first;
    bool is_upper=isupper(first_key[0]);
    for (auto &key: dict)
    {
        if (isupper(key.first[0])!=is_upper)
        return false;
    }
    return true;
}


