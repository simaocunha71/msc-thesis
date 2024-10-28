    if (strings.size()==0)
    return "None";
    int max_len=0;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max_len)
    {
        max_len=strings[i].length();
    }
    for (i=0;i<strings.size();i++)
    if (strings[i].length()==max_len)
    return strings[i];
}


