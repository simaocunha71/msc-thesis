    vector<string> prefixes;
    int i;
    for (i=0;i<str.length();i++)
    {
        prefixes.push_back(str.substr(0,i+1));
    }
    return prefixes;
}


