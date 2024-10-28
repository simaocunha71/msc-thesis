    vector<string> all_strings;
    for (int i=0;i<strings.size();i++)
    if (strings[i].find(prefix)==0)
    all_strings.push_back(strings[i]);

    return all_strings;
}

