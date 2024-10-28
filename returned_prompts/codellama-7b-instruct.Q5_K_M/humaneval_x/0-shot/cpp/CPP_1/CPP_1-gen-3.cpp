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
    vector<string> v;
    int cnt = 0;
    int i = 0;
    while(i < paren_string.size()){
        if(paren_string[i] == '(') cnt++;
        else if(paren_string[i] == ')') cnt--;
        if(cnt == 0 && paren_string[i] == ')'){
            string s = paren_string.substr(i+1, paren_string.size() - i - 1);
            v.push_back(s);
            break;
        }
        if(cnt == 0 && paren_string[i] == '('){
            string s = paren_string.substr(i+1, paren_string.size() - i - 1);
            v.push_back(s);
            break;
        }
        i++;
    }
    return v;
}

