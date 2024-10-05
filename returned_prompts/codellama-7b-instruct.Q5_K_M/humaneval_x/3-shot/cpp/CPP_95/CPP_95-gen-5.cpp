    if (dict.empty()) return false;
    bool all_lower=true;
    bool all_upper=true;
    bool some_lower=false;
    bool some_upper=false;
    for (auto const& [k,v]:dict)
    {
        if (k.empty()) continue;
        if (islower(k[0]))
        {
            if (some_upper)
            return false;
            some_lower=true;
        }
        else 
        {
            if (some_lower)
            return false;
            some_upper=true;
        }
    }
    return true;
}



