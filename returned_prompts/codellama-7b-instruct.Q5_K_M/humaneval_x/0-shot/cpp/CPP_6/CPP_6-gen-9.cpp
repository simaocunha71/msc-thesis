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
    vector<int> res;
    int level=0;
    for(int i=0;i<paren_string.size();i++){
        if(paren_string[i]=='('){
            level++;
        }
        if(paren_string[i]==')'){
            level--;
        }
        if(paren_string[i]==' '){
            res.push_back(level);
            level=0;
        }
    }
    return res;
}
