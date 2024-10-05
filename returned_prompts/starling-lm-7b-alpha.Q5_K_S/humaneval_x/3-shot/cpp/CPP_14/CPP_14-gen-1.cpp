    vector<string> all_pref;
    int i;
    for (i=0;i<str.length();i++)
    {
        all_pref.push_back(str.substr(0,i+1));
    }
    return all_pref;
}


