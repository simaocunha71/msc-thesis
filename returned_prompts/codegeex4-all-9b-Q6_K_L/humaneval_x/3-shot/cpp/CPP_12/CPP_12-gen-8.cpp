    int i;
    string longest="";
    int max_len=0;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>max_len)
        {
            longest=strings[i];
            max_len=strings[i].length();
        }
    }
    return longest;
}

