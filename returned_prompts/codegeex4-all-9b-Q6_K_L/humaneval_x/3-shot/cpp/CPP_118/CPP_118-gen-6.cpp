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

The problem with your code is that it doesn't check for unbalanced parentheses. Consider the string "( ( ) ( ) ) ( )". Your code would incorrectly report that as two groups of parentheticals. The correct answer is only one. Your code would also incorrectly report that as one group of parentheticals. The correct answer is two. Here's a corrected version.
#include <cctype>   // For std::isspace

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    int i = 0;

    while (i < paren_string.length()) {
        char chr = paren_string[i];

        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;

            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }

        // Skip spaces
        while (isspace(paren_string[++i]));
    }

    return all_parens