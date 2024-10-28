    int i;
    int max_length=-1;
    string longest_string;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>max_length)
    {
        max_length=strings[i].length();
        longest_string=strings[i];
    }
    return longest_string;
}


