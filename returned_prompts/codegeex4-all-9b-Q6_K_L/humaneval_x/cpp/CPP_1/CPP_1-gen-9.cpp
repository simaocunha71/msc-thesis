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
    int i = 0;
    while(i < paren_string.length()){
        if(paren_string[i] == '('){
            int j = i;
            int count = 0;
            while(j < paren_string.length()){
                if(paren_string[j] == '('){
                    count++;
                }else if(paren_string[j] == ')'){
                    count--;
                }
                if(count == 0){
                    paren_groups.push_back(paren_string.substr(i, j-i+1));
                    i = j + 1;
                    break;
                }
                j++;
            }
        }else{
            i++;
        }
    }
    return paren_groups;
}