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
    vector<string> paren_groups;
    string paren_group;
    for(int i=0; i<paren_string.size(); ++i){
        if(paren_string[i] == '('){
            paren_group += paren_string[i];
            while(i < paren_string.size() && paren_string[i] != ')'){
                paren_group += paren_string[i++];
            }
            if(i == paren_string.size())
                break;
            i++;
            paren_groups.push_back(paren_group);
            paren_group = "";
        }
    }
    return paren_groups;
}



