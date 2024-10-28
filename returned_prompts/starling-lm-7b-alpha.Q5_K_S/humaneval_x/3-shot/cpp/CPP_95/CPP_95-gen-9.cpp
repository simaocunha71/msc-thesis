    map<string,string>::iterator it;
    for (it=dict.begin();it!=dict.end();it++)
    if (it->second>= 'a' && it->second<= 'z')
    {
        if (!(it->first >= 'a' && it->first <= 'z'))
        return false;
    }
    if (it->second>= 'A' && it->second<= 'Z')
    {
        if (!(it->first >= 'A' && it->first <= 'Z'))
        return false;
    }
    return true;
}


