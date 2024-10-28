    if(dict.empty())
    return false;
    bool all_upper=true;
    bool all_lower=true;
    map<string,string>::iterator it;
    for (it= dict.begin(); it!=dict.end(); it++)
    {
        if (it->first[0]>='a'&&it->first[0]<='z')
        all_lower=false;
        if (it->first[0]>='A'&&it->first[0]<='Z')
        all_upper=false;
    }
    return all_lower||all_upper;
} 





