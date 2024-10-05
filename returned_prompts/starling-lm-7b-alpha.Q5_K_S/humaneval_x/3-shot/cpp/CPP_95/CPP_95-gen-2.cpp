    for (map<string,string>::iterator it=dict.begin();it!=dict.end();it++)
    if (it->first[0]>=97 && it->first[0]<=122)
    {
        if (it->second[0]>=65 && it->second[0]<=90)
        return false;
    }
    if (it->first[0]>=65 && it->first[0]<=90)
    {
        if (it->second[0]>=97 && it->second[0]<=122)
        return false;
    }
    return true;
}



