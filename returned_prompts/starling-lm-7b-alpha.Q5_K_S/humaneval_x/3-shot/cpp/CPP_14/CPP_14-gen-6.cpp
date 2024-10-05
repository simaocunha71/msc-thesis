    vector<string> all_pref;
    for (int i=0;i<str.length();i++)
    {
        string cur_pref=str.substr(0,i+1);
        all_pref.push_back(cur_pref);
    }
    return all_pref;
}



