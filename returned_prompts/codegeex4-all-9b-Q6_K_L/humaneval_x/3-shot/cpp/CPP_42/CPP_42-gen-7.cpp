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

Q1 is actually a pretty interesting problem. However, I think there's a bug in your code. Here's the problem: You're trying to find all the separate groups of parentheses, but you're not ignoring spaces. That means that if you pass in a string like "(( ))", your function will not work correctly.
I'll also point out that your function name is a little misleading. It's not separating groups of parentheses, it's separating groups of parentheses and their matching closing parentheses. If you want to separate the groups of parentheses, you'll need to modify your function.
Here's a modified version of your function that ignores spaces and separates the groups of parentheses:

#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    stack<char> paren_stack;
    string current_paren;
    for (char chr : paren_string) {
        if (chr ==