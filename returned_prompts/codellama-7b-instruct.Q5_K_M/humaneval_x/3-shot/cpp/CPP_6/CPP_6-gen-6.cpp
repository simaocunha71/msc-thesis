    vector<string> all_parens;
    int current_level=0;
    int max_level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        current_level+=1;
        if (paren_string[i]==')')
        current_level-=1;
        if (current_level>max_level)
        max_level=current_level;
    }
    return {max_level};
}


