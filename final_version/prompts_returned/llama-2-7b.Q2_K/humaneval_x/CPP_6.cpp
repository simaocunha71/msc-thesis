/*
Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens("(()()) ((())) () ((())()())")
{2, 3, 1, 3}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_nested_parens(string paren_string){
	int count[4] = {0};
	int pos = strlen(paren_string);
	for (pos-1; pos!=-1 && paren_string[pos] != ')'; pos--) {
		if (paren_string[pos] == '(') count[3]=count[2]+1,count[2]=count[0]+1;
		else if (paren_string[pos] == ')') count[1]=count[2]+1;
	}
	for (int i=1; i<4;i++) printf("%d\n",count[i]);
	return count[3];
}
