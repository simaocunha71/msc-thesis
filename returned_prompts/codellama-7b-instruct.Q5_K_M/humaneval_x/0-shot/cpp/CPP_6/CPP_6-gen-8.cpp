/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    vector<int> max_nesting;
    int max_nesting_level = 0;
    string current_group = "";
    for (int i=0; i<paren_string.length(); i++){
        if (paren_string[i] == '('){
            current_group += paren_string[i];
            continue;
        }
        if (paren_string[i] == ')'){
            current_group += paren_string[i];
            if (max_nesting_level < current_group.length()){
                max_nesting_level = current_group.length();
            }
            max_nesting.push_back(max_nesting_level);
            current_group = "";
        }
    }
    return max_nesting;
}
