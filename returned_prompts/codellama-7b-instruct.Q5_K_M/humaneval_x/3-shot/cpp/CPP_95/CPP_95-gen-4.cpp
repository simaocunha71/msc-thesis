    if (dict.size()==0) return true;
    string key;
    bool all_lower=true;
    bool all_upper=true;
    for (auto it=dict.begin();it!=dict.end();it++)
    {
        key=it->first;
        if (all_lower)
        {
        if (isupper(key[0])) all_lower=false;
        }
        if (all_upper)
        {
        if (islower(key[0])) all_upper=false;
        }
    }
    return all_lower || all_upper;
}




