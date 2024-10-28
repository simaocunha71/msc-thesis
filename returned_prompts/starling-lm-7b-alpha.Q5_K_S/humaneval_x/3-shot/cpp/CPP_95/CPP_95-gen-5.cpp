    map<string,string>::iterator it;
    bool all_lower=true;
    bool all_upper=true;
    for (it=dict.begin();it!=dict.end();it++)
    {
        string curr_key=it->first;
        if (isupper(curr_key[0]))
            all_lower=false;
        if (islower(curr_key[0]))
            all_upper=false;
    }
    return all_lower||all_upper;
}


