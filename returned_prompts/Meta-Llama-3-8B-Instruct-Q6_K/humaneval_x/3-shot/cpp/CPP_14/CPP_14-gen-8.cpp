    vector<string> prefixes;
    string prefix;
    for (int i=1;i<=str.length();i++)
    {
        prefix=str.substr(0,i);
        prefixes.push_back(prefix);
    }
    return prefixes;
}