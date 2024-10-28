    vector<int> all_levels;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        char chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
        }
        if (chr==')')
        {
            level-=1;
        }
        all_levels.push_back(level);
    }
    return all_levels;
}