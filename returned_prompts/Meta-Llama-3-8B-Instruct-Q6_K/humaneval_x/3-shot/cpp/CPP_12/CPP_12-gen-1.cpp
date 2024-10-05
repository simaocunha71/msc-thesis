    if (strings.size()==0)
    return "";
    string longest_str=strings[0];
    int longest_str_len=strings[0].length();
    for (int i=1;i<strings.size();i++)
    {
        if (strings[i].length()>longest_str_len)
        {
            longest_str=strings[i];
            longest_str_len=strings[i].length();
        }
    }
    return longest_str;
}