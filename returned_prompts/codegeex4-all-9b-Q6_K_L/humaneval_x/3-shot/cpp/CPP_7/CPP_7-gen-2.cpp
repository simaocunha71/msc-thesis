    vector<string> all_substrings;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].find(substring)!=std::string::npos)
    all_substrings.push_back(strings[i]);
    return all_substrings;
}

