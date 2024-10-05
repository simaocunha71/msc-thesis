    vector<string> all_prefixes;
    int i;
    for (i=0;i<str.length();i++)
    {
        all_prefixes.push_back(str.substr(0,i+1));
    }
    return all_prefixes;
}


