	vector<char> stk;
	for(int i = 0; i < lst[0].size(); i++)
		if(lst[0][i] == '(') stk.push_back('(');
		else if(lst[0][i] == ')'){
			if(stk.empty()) return "No";
			stk.pop_back();
		}
	if(stk.empty()){
		for(int i = 0; i < lst[1].size(); i++)
			if(lst[1][i] == '(') stk.push_back('(');
			else if(lst[1][i] == ')'){
				if(stk.empty()) return "No";
				stk.pop_back();
			}
		if(stk.empty()) return "Yes";
		else return "No";
	}else return "No";
}


#include <iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
	cout << match_parens({"()(", ")"}) << endl;
	cout << match_parens({")", ")"}) << endl;
	cout << match_parens({"(", "()"}) << endl;
	cout << match_parens({"(())()", ")"}) << endl;
	cout << match_parens({"(())()", "()("}) << endl;
}


*/

/*

match_parens({"()(", ")"}) == "Yes"
match_parens({"())", ")"}) == "No"
match_parens({"(", ")"}) == "No"
match_parens({"(", "()"}) == "Yes"
match_parens({"(())()", ")"}) == "Yes"
match_parens({"(())()", "()("}) == "No"

*/



































