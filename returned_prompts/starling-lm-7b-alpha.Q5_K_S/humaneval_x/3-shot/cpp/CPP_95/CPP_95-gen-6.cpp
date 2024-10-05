    int i;
    for (map<string,string>::iterator it=dict.begin();it!=dict.end();it++)
    if (it->first[0]!=tolower(it->first[0]) && it->first[0]!=toupper(it->first[0]))
    return false;
    return true;
}


