    vector<int> levels;
    int level=0;
    string current_paren;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren+=chr;
            levels.push_back(level);
            current_paren="";
        }
    }
    return levels;
}