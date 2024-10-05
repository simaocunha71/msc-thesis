    if  (strings.empty())
    return "";

    string longest_string = strings[0];
    int i;
    for  (i=1;i<strings.size();i++)
    {
        if  (strings[i].length()>longest_string.length())
        longest_string=strings[i];
    }
    return longest_string;
}


