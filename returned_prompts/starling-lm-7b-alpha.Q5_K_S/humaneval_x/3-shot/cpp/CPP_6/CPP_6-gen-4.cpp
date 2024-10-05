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
        }
        if (i==paren_string.length()-1||paren_string[i+1]==' '){
            all_parens.push_back(level);
            current_paren="";
            level=0;
        }
    }
    return all_parens;
}


