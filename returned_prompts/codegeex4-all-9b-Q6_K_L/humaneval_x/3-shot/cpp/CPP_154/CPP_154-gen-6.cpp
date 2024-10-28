
The first function looks correct. There's no need to do anything else.
The second function has a bug. Here is your code, with the bug highlighted:
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

You're checking if the level is zero, and then if it is, you're pushing the current_paren into the vector. This means that the last parenthesis group is pushed in, even though the level is not yet zero. You should change it to this:
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
    if (level != 0) {
        // Error, unbalanced parentheses
        // TODO: return error or whatever
    }
    return all_parens;

The third function is correct.
The fourth function is correct.