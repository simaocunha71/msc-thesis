    vector<string> all_prefixes;
    string current_prefix="";
    int i;
    for (i=0;i<str.length();i++)
    {
        current_prefix+=str[i];
        all_prefixes.push_back(current_prefix);
    }
    return all_prefixes;
}

