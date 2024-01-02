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
	int open=0, close=0;
	for(auto i = 0;i < lst.size(); ++i) {
	if (lst[i] == "(" )
	open++;
	else if(lst[i] == ")")
	close++;
	}
	int count=(close-open);
	string res="Yes";
	if(count==0){
		res=lst.at(0)+"No";
	}

return res;
}

int main(){
	// Your code here
	vector<string> l = {"(()", "))"} ;
    string s = match_parens (l);
    printf("%s\n", s.c_str());
	return 0;
}