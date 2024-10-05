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
    string res = "";
    for(string s: lst){
        res += s;
    }
    int balance = 0;
    for(char c: res){
        if(c == '(') balance++;
        else balance--;
        if(balance < 0) return "No";
    }
    return "Yes";
}
int main(){
    vector<string> lst;
    lst.push_back("()(");
    lst.push_back(")");
    printf("%s", match_parens(lst).c_str());
    return 0;
}
