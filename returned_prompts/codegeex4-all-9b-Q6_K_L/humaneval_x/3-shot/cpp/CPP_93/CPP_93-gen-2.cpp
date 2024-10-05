    vector<string> all_parens;
    stringstream current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            level+=1;
            current_paren << chr;
        }
        if (chr==')')
        {
            level-=1;
            current_paren << chr;
            if (level==0){
                all_parens.push_back(current_paren.str());
                current_paren.str("");
