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
	int last_index = 0, open_count=1, cur_count=1;
	if (open_count == 2)
	{
		for (int i=1; i<=paren_string.length();i++){
			if (paren_string[i] == '('){
				last_index = i - 1;
			}
			else if(paren_string[i]==')'){
				cur_count--;
			}
			if (cur_count == 0)
			open_count++;
		}
	}
	vector<string> temp = { };
	for(int i=0;i<paren_string.length();i++){
		if (paren_string[i] == '('){
			temp.push_back("()");
		}
		else if(paren_string[i]==')'){
			cur_count--;
		}
		if (open_count == cur_count) {
			for(int j=0;j<last_index-1;j++)
			{
				temp.push_back("()");
			}
			temp[temp.size()-1] += "()";
			i--; 
		}
	}
	for (int i = open_count + 1; i<=paren_string.length(); i++) { 
		if