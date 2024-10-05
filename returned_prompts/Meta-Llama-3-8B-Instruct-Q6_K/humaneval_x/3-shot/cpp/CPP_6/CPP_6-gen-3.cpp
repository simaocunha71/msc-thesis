    vector<int> levels;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
            level++;
        if (paren_string[i]==')')
            level--;
        levels.push_back(level);
    }
    return levels;
}