    vector<int> levels;
    int level=0;
    char chr;
    int i;
    for  (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if  (chr=='(')
        level+=1;
        if  (chr==')')
        {
            levels.push_back(level);
            level-=1;
        }
    }
    return levels;
}


