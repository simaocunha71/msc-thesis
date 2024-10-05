    for (map<string,string>::iterator it=dict.begin();it!=dict.end();it++)
    {
        if (it->second=="")
        continue;
        if (!(isupper(it->first[0]) && isupper(it->second[0])) && 
        !(islower(it->first[0]) && islower(it->second[0])))
        return false;
    }
    return true;
}





