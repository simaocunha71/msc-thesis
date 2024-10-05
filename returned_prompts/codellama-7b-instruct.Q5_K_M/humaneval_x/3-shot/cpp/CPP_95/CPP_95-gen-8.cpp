    if (dict.size()==0)
    return false;

    bool is_all_lower=true;
    bool is_all_upper=true;
    for (auto x:dict)
    {
        if (x.first.find_first_not_of("[a-z]") != string::npos)
        {
        is_all_lower=false;
        }
        if (x.first.find_first_not_of("[A-Z]") != string::npos)
        {
        is_all_upper=false;
        }
    }
    return (is_all_lower || is_all_upper);
}



