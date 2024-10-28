    if(dict.empty())
        return false;
    bool all_lower = true, all_upper = true;
    for (auto it = dict.begin(); it != dict.end(); ++it)
    {
        for (int i = 0; i < it->first.size(); i++)
        {
            if (islower(it->first[i])) 
                all_upper = false;
            if (isupper(it->first[i])) 
                all_lower = false;
        }
    }
    return all_lower || all_upper;
}


