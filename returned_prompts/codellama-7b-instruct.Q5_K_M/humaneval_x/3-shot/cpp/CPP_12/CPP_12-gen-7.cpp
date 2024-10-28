    if (strings.size()==0)
        return "";
    int max_length=0;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max_length)
    {
        max_length=strings[i].length();
    }
    for (i=0;i<strings.size();i++)
    if (strings[i].length()==max_length)
    return strings[i];
}


