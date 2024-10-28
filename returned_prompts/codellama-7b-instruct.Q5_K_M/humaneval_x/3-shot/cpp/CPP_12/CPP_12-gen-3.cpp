    if (strings.size()==0)
    return "";
    int i;
    int longest_len=0;
    string longest_str="";
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>longest_len)
        {
            longest_len=strings[i].length();
            longest_str=strings[i];
        }
    }
    return longest_str;
}


