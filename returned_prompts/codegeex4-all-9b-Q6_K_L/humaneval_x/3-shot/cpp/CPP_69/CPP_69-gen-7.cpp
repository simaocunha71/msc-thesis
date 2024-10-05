
Your has_close_elements function is correct.  It's a good start!
Your separate_paren_groups function is almost correct, but you need to handle an empty string, which can happen if the parentheses are unbalanced or nested in a way that doesn't match your logic.  For example, separate_paren_groups("( ( ) )") should return {"()", "()"}.  You can add a check at the start of your function to return an empty vector if the input string is empty.  Also, you should check for an unbalanced string at the end of your function.  If level is not zero, then the parentheses are unbalanced, so you should return an empty vector.
Your truncate_number function is correct.
Your search function is correct.

Here's a corrected version of separate_paren_groups:
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;

    if (paren_string.empty()) {
        return all_parens;
    }

    for (i=0; i<paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        }
        if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }

    if (level != 0) {
        all_parens.clear();
    }

    return all_parens;
}