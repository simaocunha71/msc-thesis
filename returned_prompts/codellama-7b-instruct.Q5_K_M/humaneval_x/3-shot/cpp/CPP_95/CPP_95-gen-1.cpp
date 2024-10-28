    int i=0;
    string key;
    bool lower=true;
    bool upper=true;
    map<string,string>::iterator it;
    for (it=dict.begin();it!=dict.end();it++)
    {
        i++;
        key=it->first;
        if (i==1)
        {
            if (key[0]>='A' && key[0]<='Z')
            upper=false;
            if (key[0]>='a' && key[0]<='z')
            lower=false;
        }
        if (upper && key[0]>='a' && key[0]<='z')
        upper=false;
        if (lower && key[0]>='A' && key[0]<='Z')
        lower=false;
        if (lower && upper)
        return false;
    }
    return true;
}


