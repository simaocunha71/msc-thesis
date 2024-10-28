    if (strings.empty()) return "";

    int i;
    string longest_str="";
    for (i=0;i<strings.size();i++)
    if (strings[i].length()>longest_str.length())
    longest_str=strings[i];

    return longest_str;
}


