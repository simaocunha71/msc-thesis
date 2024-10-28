    if (dict.empty()) return false;
    bool is_lower=true;
    bool is_upper=true;
    for (auto it=dict.begin();it!=dict.end();it++)
    {
        if (is_lower&&it->first[0]>='A'&&it->first[0]<='Z')
            is_lower=false;
        if (is_upper&&it->first[0]>='a'&&it->first[0]<='z')
            is_upper=false;
        if (is_lower&&is_upper)
            return false;
    }
    return true;
}



