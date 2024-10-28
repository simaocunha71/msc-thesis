    vector<string> all_prefixes;
    string prefix;
    int i;
    for (i=0;i<str.length();i++)
    {
        prefix="";
        for (int j=0;j<=i;j++)
        {
            prefix+=str[j];
            all_prefixes.push_back(prefix);
        }
    }
    return all_prefixes;
}




