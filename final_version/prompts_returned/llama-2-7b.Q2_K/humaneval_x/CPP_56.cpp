/*
brackets is a string of '<' and '>'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
false
>>> correct_bracketing("<>")
true
>>> correct_bracketing("<<><>>")
true
>>> correct_bracketing("><<>")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
	int j=0,i=0,k=0; 
	for (int i = 0; i < brackets.size(); ++i) {
		if (brackets[i] == '>'){
			j++;
		}else if(brackets[i+1]=='<'){
		k=j-1;
		}
		else
		k--;
		printf("%c\t%d\n", brackets[i], k);
	}
return j>0;

}

int main(){
	string brackets;
	scanf(" %s ", brackets.c_str());
	correct_bracketing(brackets);
	return 0;
}