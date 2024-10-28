    int i;
    int max=0;
    string max_string;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max)
    {
        max_string=strings[i];
        max=strings[i].length();
    }
    return max_string;
}

