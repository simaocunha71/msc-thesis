    vector<string> all_prefixes;
    for (int i=0;i<str.length();i++)
    all_prefixes.push_back(str.substr(0,i+1));
    return all_prefixes;
}

