    vector<int> all_levels;
    string current_paren;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        char chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            all_levels.push_back(level);
            current_paren="";
        }
    }
    return all_levels;
}