    int i;
    vector<string> filtered_strings;
    for (i=0;i<strings.size();i++)
    if (strings[i].find(substring)!=string::npos)
    filtered_strings.push_back(strings[i]);
    return filtered_strings;
}

