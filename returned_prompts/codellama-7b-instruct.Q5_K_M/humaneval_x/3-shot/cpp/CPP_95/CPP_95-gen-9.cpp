    if (dict.size()==0)
    return true;

    bool all_lower=true, all_upper=true;
    for (auto i=dict.begin();i!=dict.end();i++)
    {
        if (i->first.find_first_not_of("abcdefghijklmnopqrstuvwxyz")!=string::npos)
        all_lower=false;

        if (i->first.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZ")!=string::npos)
        all_upper=false;

        if (!all_lower && !all_upper)
        return false;
    }

    return true;
}




