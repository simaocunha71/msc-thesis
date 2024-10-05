/*
Input to this function is a string with parentheses.
Output is a vector of integers that indicate the deepest level of nesting of parentheses.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    vector<int> res;
    int depth = 0;
    for (int i = 0; i < paren_string.size(); i++){
        if (paren_string[i] == '('){
            depth++;
        }
        else if (paren_string[i] == ')'){
            depth--;
        }
        if (depth > res.size())
            res.push_back(depth);
    }
    return res;
}

B:
/*
Input to this function is a vector of integers that indicate the deepest level of nesting of parentheses.
Output is a string with parentheses.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string parse_nested_parens(vector<int> depth_vector){
    string res = "";
    for (int i = 0; i < depth_vector.size(); i++){
        res += string(depth_vector[i], '(');
        res += string(depth_vector[i], ')');
    }
    return res;
}

C:
/*
Input to this function is a string with parentheses.
Output is a vector of integers that indicate the deepest level of nesting of parentheses.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
    vector<int> res;
    int depth = 0;
    for (int i = 0; i < paren_string.size(); i++){
        if (paren_string[i] == '('){
            depth++;
        }
        else if (paren_string[i] == ')'){
            depth--;
        }
        if (depth > res.size())
            res.