    vector<string> all_parens;
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
            if (level==0){
                all_parens.push_back(current_paren);
                current_paren="";
            }
        }
    }
    return all_parens;
}

This function looks fine, but it's going to fail if there are any spaces in the input string. You should remove the spaces before processing the string.

/*
Given a positive floating point number, it can be decomposed into
and integer part (largest integer smaller than given number) and decimals
(leftover part always smaller than 1).

Return the decimal