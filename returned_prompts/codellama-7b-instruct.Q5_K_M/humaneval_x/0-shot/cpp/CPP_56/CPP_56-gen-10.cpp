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
	int l=brackets.size();
	int c=0;
	for(int i=0;i<l;i++){
		if(brackets[i]=='<'){
			c++;
		}
		else if(brackets[i]=='>'){
			c--;
		}
		if(c<0){
			return false;
		}
	}
	return (c==0)? true : false;
}
//test case
int main(){
	string brackets;
	cin>>brackets;
	if(correct_bracketing(brackets)){
		printf("true\n");
	}
	else{
		printf("false\n");
	}
	return 0;
}
