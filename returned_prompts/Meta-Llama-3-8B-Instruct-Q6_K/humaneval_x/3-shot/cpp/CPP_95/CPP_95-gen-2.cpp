    if(dict.empty())
        return false;
    bool all_lower = true;
    bool all_upper = true;
    map<string,string>::iterator it;
    for(it=dict.begin();it!=dict.end();it++)
    {
        if((it->first)[0] >= 'a' && (it->first)[0] <= 'z')
            all_upper = false;
        else if((it->first)[0] >= 'A' && (it->first)[0] <= 'Z')
            all_lower = false;
        else
            return false;
    }
    return (all_lower || all_upper);
}