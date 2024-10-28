    map<string,string>::iterator it;
    bool all_upper=true, all_lower=true;
    for (it=dict.begin();it!=dict.end();it++)
    {
        if (it->second[0]>='a' && it->second[0]<='z')
        {
        all_upper=false;
        }
        if (it->second[0]>='A' && it->second[0]<='Z')
        {
        all_lower=false;
        }
    }
    if (all_upper||all_lower) return true;
    return false;
}



