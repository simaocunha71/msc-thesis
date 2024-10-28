    int max_length=0;
    string longest_string="";
    for (int i=0;i<strings.size();i++)
    {
    if (strings[i].length()>max_length)
    {
        max_length=strings[i].length();
        longest_string=strings[i];
    }
    }
    return longest_string;
}

