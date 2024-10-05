    vector<int> max_levels;
    vector<int> current_levels;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_levels.push_back(level);
        }
        if (chr==')')
        {
            level-=1;
            current_levels.pop_back();
        }
    }
    int max_level=0;
    for (i=0;i<current_levels.size();i++)
        max_level=max(max_level,current_levels[i]);
    max_levels.push_back(max_level);
    return max_levels;
}


