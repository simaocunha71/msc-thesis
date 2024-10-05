    if (strings.size()==0)
        return "";
    int longest_length=0;
    int i;
    string longest_string;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>longest_length)
        {
            longest_string=strings[i];
            longest_length=strings[i].length();
        }
    }
    return longest_string;
}


