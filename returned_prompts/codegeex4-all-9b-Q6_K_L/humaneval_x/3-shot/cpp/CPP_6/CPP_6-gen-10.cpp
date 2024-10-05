    vector<int> max_levels;
    int level=0;
    char chr;
    int i;
    int max_level=0;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
        level+=1;
        if (level>max_level)
        max_level=level;
        }
        if (chr==')')
        {
            level-=1;
        }
        if (chr==' ')
        {
            max_levels.push_back(max_level);
            max_level=0;
            level=0;
        }
    }
    return max_levels;
}

