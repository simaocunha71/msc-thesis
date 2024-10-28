    vector<int> deepest_levels;
    int deepest_level=0;
    int current_level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        current_level+=1;
        if (paren_string[i]==')')
        current_level-=1;
        if (current_level>deepest_level)
        deepest_level=current_level;
    }
    deepest_levels.push_back(deepest_level);
    return deepest_levels;
}



