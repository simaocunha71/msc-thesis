    vector<string> all_pref;
    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        all_pref.push_back(string("")+chr);
        for (int j=0;j<i;j++)
        all_pref[i]+=str[j];
    }
    return all_pref;
}


