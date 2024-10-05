    vector<string> all_strings;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].compare(0,prefix.length(),prefix)==0)
    all_strings.push_back(strings[i]);
    return all_strings;
}

