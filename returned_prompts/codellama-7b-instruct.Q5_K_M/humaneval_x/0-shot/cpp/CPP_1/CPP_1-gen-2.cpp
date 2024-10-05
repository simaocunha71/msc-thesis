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

vector<string> groups;
int i = 0;
string group = "";
while(i < paren_string.length()){
if(paren_string[i] == '('){
group += paren_string[i];
i++;
while(paren_string[i] != ')'){
group += paren_string[i];
i++;
}
i++;
group += paren_string[i];
groups.push_back(group);
group = "";
}
i++;
}
return groups;
}

