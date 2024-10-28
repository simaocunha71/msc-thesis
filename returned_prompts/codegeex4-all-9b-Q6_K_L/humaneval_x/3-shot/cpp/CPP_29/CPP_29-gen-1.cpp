    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<strings.size();i++)
    if (strings[i][0]==prefix[0])
    all_parens.push_back(strings[i]);
    return all_parens;
}

