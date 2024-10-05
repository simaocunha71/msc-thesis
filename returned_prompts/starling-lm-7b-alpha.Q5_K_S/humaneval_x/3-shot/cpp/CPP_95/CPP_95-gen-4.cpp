    map<string,string>::iterator itr;
    for (itr=dict.begin();itr!=dict.end();itr++)
    {
        string key=itr->first;
        string value=itr->second;
        if (key[0]!=toupper(key[0]) && key[0]!=tolower(key[0]))
        return false;
    }
    return true;
}



