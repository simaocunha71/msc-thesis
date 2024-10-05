    vector<string> filtered_strings;
    string s;
    int i;
    for (i=0;i<strings.size();i++)
    {
        s=strings[i];
        if (s.find(substring)!=string::npos)
        filtered_strings.push_back(s);
    }
    return filtered_strings;
}


