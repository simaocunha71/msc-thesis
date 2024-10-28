    vector<string> filtered_strings;
    for (int i=0;i<strings.size();i++)
    if (strings[i].substr(0,prefix.length())==prefix)
    filtered_strings.push_back(strings[i]);
    return filtered_strings;
}

