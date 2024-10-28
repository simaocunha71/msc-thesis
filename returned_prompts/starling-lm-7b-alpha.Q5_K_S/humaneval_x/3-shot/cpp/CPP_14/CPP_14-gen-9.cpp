    vector<string> all_prefixes;
    int i;
    int len=str.length();
    for (i=0;i<len;i++)
    {
        all_prefixes.push_back(str.substr(0,i+1));
    }
    return all_prefixes;
}


