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
    vector<int> output;
    int max_depth = 0;
    int current_depth = 0;
    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            current_depth++;
            if(current_depth > max_depth){
                max_depth = current_depth;
            }
        }else if(paren_string[i] == ')'){
            current_depth--;
        }else if(paren_string[i] == ' '){
            output.push_back(max_depth);
            max_depth = 0;
            current_depth = 0;
        }
    }
    output.push_back(max_depth);
    return output;
}
