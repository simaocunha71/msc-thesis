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
    vector<int> result;
    int i = 0;
    while(i < paren_string.size()){
        int depth = 0;
        int max_depth = 0;
        while(paren_string[i] != ')'){
            if(paren_string[i] == '('){
                depth++;
                if(depth > max_depth) max_depth = depth;
            }
            i++;
        }
        result.push_back(max_depth);
        i++;
    }
    return result;
}

C:
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
    vector<int> result;
    int i = 0;
    while(i < paren_string.size()){
        int depth = 0;
        int max_depth = 0;
        while(paren_string[i] != ')'){
            if(paren_string[i] == '('){
                depth++;
                if(depth > max_depth) max_depth = depth;
            }
            i++;
        }
        result.push_back(max_depth);
        i++;
    }
    return result;
}

D:
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
    vector<int>