    vector<int> levels;
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
        levels.push_back(level);
    }
    return levels;
}  // end of function parse_nested_parens


