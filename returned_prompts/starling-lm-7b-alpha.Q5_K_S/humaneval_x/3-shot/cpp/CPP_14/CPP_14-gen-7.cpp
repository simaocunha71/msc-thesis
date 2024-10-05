    vector<string> all_prefixes;
    int i,j;
    char chr;
    for (i=0;i<str.length();i++)
    {
        all_prefixes.push_back("");
        for (j=i;j<str.length();j++)
        {
            chr=str[j];
            all_prefixes[all_prefixes.size()-1]+=chr;
        }
    }
    return all_prefixes;
}


