    if(strings.empty())
        return "";
    string longest_str=strings[0];
    for (int i=1;i<strings.size();i++)
    {
        if(strings[i].length()>longest_str.length())
            longest_str=strings[i];
    }
    return longest_str;
}

