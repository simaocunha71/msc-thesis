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
    int max_nesting = 0;
    vector<int> nesting_levels;
    for(string::size_type i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            nesting_levels.push_back(0);
            max_nesting = max(max_nesting, nesting_levels.size()-1);
        }
        else if(paren_string[i] == ')'){
            if(max_nesting == nesting_levels.size()-1){
                nesting_levels.pop_back();
            }
            else{
                nesting_levels[nesting_levels.size()-2]++;
            }
        }
    }
    return nesting_levels;
}

