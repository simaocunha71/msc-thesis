    int i;
    vector<string> filtered;
    for (i=0;i<strings.size();i++)
    if (strings[i].find(substring)!=string::npos)
    filtered.push_back(strings[i]);
    return filtered;
}



