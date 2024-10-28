    if(strings.empty())return "";
    string longest_str=strings[0];
    for (string s : strings)
    {
        if (s.length()>longest_str.length())
        longest_str=s;
    }
    return longest_str;
}  // This will return the first longest string if there are multiple strings with the same length


