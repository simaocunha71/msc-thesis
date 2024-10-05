    vector<string> all_prefixes;
    int i;
    for (i=0;i<str.length();i++)
    {
        string current_prefix=str.substr(0,i+1);
        all_prefixes.push_back(current_prefix);
    }
    return all_prefixes;
}


