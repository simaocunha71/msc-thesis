    int size=dict.size();
    string first_key=dict.begin()->first;
    bool is_lower=false;
    bool is_upper=false;
    for (auto i:dict)
    {
        if (is_lower==false)
        {
        is_lower=islower(i.first[0]);
        }
        if (is_upper==false)
        {
        is_upper=isupper(i.first[0]);
        }
        if (is_lower==true && is_upper==true)
        return false;
        if (i.first!=first_key)
        return false;
    }
    return true;
}



