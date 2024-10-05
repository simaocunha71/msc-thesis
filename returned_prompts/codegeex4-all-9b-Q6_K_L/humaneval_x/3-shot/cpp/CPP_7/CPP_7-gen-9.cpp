    vector<string> all_strings;
    int i,j;
    for (i=0;i<strings.size();i++)
    {
    for (j=0;j<strings[i].length();j++)
    if (strings[i][j]==substring[0])
    all_strings.push_back(strings[i]);
    }
    return all_strings;
}

