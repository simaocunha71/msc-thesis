    if (strings.size()==0)
    return "";
    int max_len=0;
    string longest_string;
    for (int i=0;i<strings.size();i++)
    if (strings[i].length()>max_len)
    {
        max_len=strings[i].length();
        longest_string=strings[i];
    }
    return longest_string;
}

