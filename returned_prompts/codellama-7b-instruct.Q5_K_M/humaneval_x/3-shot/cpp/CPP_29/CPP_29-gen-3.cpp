    vector<string> filtered;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].compare(0,prefix.length(),prefix)==0)
    filtered.push_back(strings[i]);
    return filtered;
}


