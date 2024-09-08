/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    vector<int> result;
    int i = 0;
    while(i < paren_string.size()){
        int level = 0;
        int max_level = 0;
        while(i < paren_string.size() && paren_string[i] != ')'){
            if(paren_string[i] == '('){
                level++;
                if(level > max_level){
                    max_level = level;
                }
            }
            i++;
        }
        result.push_back(max_level);
        i++;
    }
    return result;
}

/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    vector<int> result;
    int i = 0;
    while(i < paren_string.size()){
        int level = 0;
        int max_level = 0;
        while(i < paren_string.size() && paren_string[i] != ')'){
            if(paren_string[i] == '('){
                level++;
                if(level > max_level){
                    max_level = level;
                }
            }
            i++;
        }
        result.push_back(max_level);
        i++;
    }
    return result;
}

/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3