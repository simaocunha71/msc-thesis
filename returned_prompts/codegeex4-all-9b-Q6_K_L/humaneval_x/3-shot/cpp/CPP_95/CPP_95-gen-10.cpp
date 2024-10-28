    int i=0;
    map<string,string>::iterator it;
    for (it=dict.begin();it!=dict.end();it++)
    {
        if (isupper(it->first[0]))
        i+=1;
    }
    if (i==dict.size())
    return true;
    i=0;
    for (it=dict.begin();it!=dict.end();it++)
    {
        if (islower(it->first[0]))
        i+=1;
    }
    if (i==dict.size())
    return true;
    return false;
}

