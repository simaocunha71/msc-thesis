    string longest_string="";
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>longest_string.length())
    longest_string=strings[i];

    return longest_string;
}


