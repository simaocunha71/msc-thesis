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
using namespace std;
vector<string> separate_paren_groups(string paren_string){
    vector<string> result;
    int current = 0;
    int last = 0;
    int level = 0;
    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            level++;
        }else if(paren_string[i] == ')'){
            level--;
        }
        if(paren_string[i] == ')' && level == 0){
            result.push_back(paren_string.substr(last, i - last + 1));
            last = i + 1;
        }
    }
    result.push_back(paren_string.substr(last));
    return result;
}