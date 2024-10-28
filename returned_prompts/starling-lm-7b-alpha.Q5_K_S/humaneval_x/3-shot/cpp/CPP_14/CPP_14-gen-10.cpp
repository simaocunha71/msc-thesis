    vector<string> all_pref;
    string current_pref;
    int i;
    for (i=0;i<str.length();i++)
    {
        current_pref+=str[i];
        all_pref.push_back(current_pref);
    }
    return all_pref;
}


