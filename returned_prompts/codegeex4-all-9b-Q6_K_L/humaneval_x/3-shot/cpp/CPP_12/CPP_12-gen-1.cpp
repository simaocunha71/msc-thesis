    string longest_str;
    int i;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].size()>longest_str.size())
        longest_str=strings[i];
    }
    return longest_str;
}