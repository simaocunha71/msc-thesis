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
	int i = 0;
	int count = 0;
	bool answer = true;
	while (i < brackets.length() && answer){
		if (brackets[i] == '<'){
			count++;
		}
		else if (brackets[i] == '>'){
			count--;
			if (count < 0){
				answer = false;
			}
		}
		i++;
	}
	if (count != 0){
		answer = false;
	}
	return answer;
}
