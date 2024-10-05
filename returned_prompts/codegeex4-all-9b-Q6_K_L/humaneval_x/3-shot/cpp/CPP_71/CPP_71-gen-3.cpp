
You have a problem with the second question. You are not accounting for the possibility of the input string ending with an open parenthesis. For example, if you call your function with the string "(())(", your function will return an empty string for the first group and an empty string for the second group, but the string should be split into three groups: {"()", "()", ""}.
Here is a corrected version of the function:
vector<string> separate_paren_groups(string paren_string){
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
    // Add the last group if the string ended with an open parenthesis
    if (level > 0) {
        all_parens.push_back(current_paren);
    }
    return all_parens;
}