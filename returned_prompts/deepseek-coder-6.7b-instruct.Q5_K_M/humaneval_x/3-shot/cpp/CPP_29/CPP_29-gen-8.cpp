    vector<string> filtered;
    for(int i=0;i<strings.size();i++)
    if(strings[i].substr(0,prefix.size())==prefix)
    filtered.push_back(strings[i]);
    return filtered;
}


