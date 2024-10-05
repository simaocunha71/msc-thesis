    int i;
    int max=0;
    string longest_str;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max)
    {
        max=strings[i].length();
        longest_str=strings[i];
    }
    return longest_str;
}


