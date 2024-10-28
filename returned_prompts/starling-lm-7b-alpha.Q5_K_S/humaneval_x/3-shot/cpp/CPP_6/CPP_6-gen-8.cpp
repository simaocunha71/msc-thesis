    vector<int> all_parens;
    string current_paren;
    int level=0;
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
            if (level>all_parens.back())
                all_parens.back()=level;
        }
        if (i==paren_string.length()-1 || paren_string[i+1]==' ')
        {
            if (level>all_parens.back())
                all_parens.back()=level;
            else
                all_parens.push_back(level);

            current_paren="";
        }
    }
    return all_parens;
}

