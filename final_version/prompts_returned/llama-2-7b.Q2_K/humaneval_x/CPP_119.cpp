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
	int open_cnt = 0, close_cnt = 0;
	ifstream ins("in.txt");
	ofstream out("out.txt");
	for(auto it : lst) {
		open_cnt += it[0] == '(' ? 1 : -1;
		close_cnt += it[it.size()-1] == ')' ? 1: -1;
	}
	if(!(open_cnt > close_cnt)) return "No";
	string ans;
	while((!ans.empty()) && (open_cnt <= 0 || open_cnt >= close_cnt) ) {
		for(int i = 0;i < lst.size();++i){
			if(!ans[ans.size()-1] == ')' && lst[i][lst[i].size() - 1] == ')'){
				i--, ans += lst[i];
			}else if(lst[i][lst[i].size() - 1]=='(' && ans.back() != '('){
				if(!ans) break;
				break;
			}
		}
	}
	out<<(open_cnt <= 0 || open_cnt >= close_cnt? "No": ""<<"(");