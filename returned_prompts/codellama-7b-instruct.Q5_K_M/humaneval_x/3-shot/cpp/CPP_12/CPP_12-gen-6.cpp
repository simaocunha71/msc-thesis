    int longest_len=-1;
    int i;
    string longest_string="";
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>longest_len)
        {
        longest_len=strings[i].length();
        longest_string=strings[i];
        }
    }
    return longest_string;
}


