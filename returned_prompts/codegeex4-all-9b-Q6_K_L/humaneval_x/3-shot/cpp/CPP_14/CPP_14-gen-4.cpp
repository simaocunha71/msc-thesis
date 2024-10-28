    vector<string> all_prefix;
    int i;
    for (i=0;i<str.length();i++)
    {
        all_prefix.push_back(str.substr(0,i+1));
    }
    return all_prefix;
}

