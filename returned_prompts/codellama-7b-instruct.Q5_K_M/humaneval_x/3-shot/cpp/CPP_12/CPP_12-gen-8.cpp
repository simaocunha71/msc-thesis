    int longest_length=0;
    string longest_string="";
    if (strings.size()==0)
    return "";
    for (int i=0;i<strings.size();i++)
    {
        if (strings[i].length()>longest_length)
        {
            longest_length=strings[i].length();
            longest_string=strings[i];
        }
    }
    return longest_string;
}



