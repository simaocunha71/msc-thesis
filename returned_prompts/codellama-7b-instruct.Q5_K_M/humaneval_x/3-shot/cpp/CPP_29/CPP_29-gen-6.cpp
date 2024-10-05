    vector<string> prefixed_strings;
    string s;
    int i;
    for (i=0;i<strings.size();i++)
    {
        s=strings[i];
        if (s.find(prefix)==0)
        prefixed_strings.push_back(s);
    }
    return prefixed_strings;
}



