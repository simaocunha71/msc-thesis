    vector<string> filtered;
    int i;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].substr(0,prefix.length())==prefix)
        filtered.push_back(strings[i]);
    }
    return filtered;
}

