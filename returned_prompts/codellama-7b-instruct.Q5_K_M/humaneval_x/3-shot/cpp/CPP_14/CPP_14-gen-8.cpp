    vector<string> all_prefixes;
    int i;
    for (i=0;i<str.length();i++)
    {
        string prefix="";
        for (int j=0;j<=i;j++)
            prefix+=str[j];
        all_prefixes.push_back(prefix);
    }
    return all_prefixes;
}


