/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "(()())"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<stack>
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> paren_groups;
    stack<char> s;
    string current_group;
    for(char c : paren_string){
        if(c == '('){
            s.push(c);
            current_group += c;
        }else if(c == ')'){
            s.pop();
            current_group += c;
            if(s.empty()){
                paren_groups.push_back(current_group);
                current_group = "";
            }
        }
    }
    return paren_groups;
}