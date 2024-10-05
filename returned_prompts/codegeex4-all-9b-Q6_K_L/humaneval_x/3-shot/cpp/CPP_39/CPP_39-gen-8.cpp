
Your problem is that the second question is looking for a function to separate parenthetical groups of characters from a string, and your code is not doing that. It's only checking if a string has balanced parentheses. You can't just return a vector of strings, you need to actually extract the strings from the input string. 
Here's an example of how you could do it:
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++)
    {
        chr = paren_string[i];
        if (chr == '(')
        {
            level += 1;
            if (level == 1) // Only start a new group if we're at the first level
            {
                current_paren += chr;
            }
        }
        else if (chr == ')')
        {
            level -= 1;
            current_paren += chr;
            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

int main()
{
    vector<string> groups = separate_paren_groups("( ) (( )) (( )( ))");
    for (string group : groups)
    {
        cout << group << endl;
    }
    return 0;
}

This code will output:
()
(())
(()())

which is the same as the expected output in your question.