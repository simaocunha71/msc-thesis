/*
brackets is a string of '(' and ')'.
return true if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("(")
false
>>> correct_bracketing("()")
true
>>> correct_bracketing("(()())")
true
>>> correct_bracketing(")(()")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
	int n=0,m=0;
	char ch1[3];
	for (ch1[2]=ch1[0]=='('?n++:m++;)
	if (ch1[2]!='('&&ch1[2]!=')'||(ch1[2]==')'&&m<n)) return false;
	return true;
}