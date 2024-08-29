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
#include<math.h>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){

B:
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
#include<math.h>
#include<vector>
#include<string>
using namespace std;
string match_parens(vector<string> lst){
    int i, j, l1, l2, l;
    char *s, *t;

    l1 = lst[0].length();
    l2 = lst[1].length();
    l = l1 + l2;
    s = (char *)malloc(sizeof(char) * l);
    t = (char *)malloc(sizeof(char) * l);

    for(i = 0; i < l1; i++){
        s[i] = lst[0][i];
    }
    for(j = 0; j < l2; j++){
        s[i + j] = lst[1][j];
    }
    for(i = 0; i < l; i++){
        t[i] = s[l - 1 - i];
    }

    for(i