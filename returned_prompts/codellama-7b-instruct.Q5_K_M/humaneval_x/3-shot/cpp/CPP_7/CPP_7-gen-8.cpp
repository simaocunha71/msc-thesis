    vector<string> result;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i].find(substring)!=-1)
    result.push_back(strings[i]);
    return result;
}


