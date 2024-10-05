    vector<string> new_strings;
    for (int i=0;i<strings.size();i++)
    if (strings[i].find(substring)!=string::npos)
        new_strings.push_back(strings[i]);
    return new_strings;
}

