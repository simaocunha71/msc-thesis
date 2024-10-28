/*
You are given a vector of two strings, both strings consist of open
parentheses '(' or close parentheses ')' only.
Your job is to check if it is possible to concatenate the two strings in
some order, that the resulting string will be good.
A string S is considered to be good if and only if all parentheses in S
are balanced. For example: the string "(())()" is good, while the string
"())" is not.
Return "Yes" if there's a way to make a good string, and return "No" otherwise.

Examples:
match_parens({"()(", ")"}) == "Yes"
match_parens({")", ")"}) == "No"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){

    stack<char> s;
    for(int i = 0; i < lst[0].size(); i++){
        if(lst[0][i] == '('){
            s.push(lst[0][i]);
        }else if(lst[0][i] == ')'){
            if(s.empty()) return "No";
            s.pop();
        }
    }
    if(s.empty()){
        s.push('(');
        for(int i = 0; i < lst[1].size(); i++){
            if(lst[1][i] == ')'){
                s.push(lst[1][i]);
            }else if(lst[1][i] == '('){
                if(s.empty()) return "No";
                s.pop();
            }
        }
    }
    if(s.empty()) return "Yes";
    return "No";
}


