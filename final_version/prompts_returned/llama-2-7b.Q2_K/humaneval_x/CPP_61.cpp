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
	int j=0,i=0,k=0; 
	for (i = 1; i < brackets.length()-2 ; ++i) {
		if ((!k && brackets[j] == '(')) //if first parenthesis is open then reset counter
		else if(brackets[j+1]==')' && brackets[j]=="(") //if last bracket is close and current counter was reset then increment it.
		{ k=0; } else {k+=1;} 
		if (k >= 2)//if k>=2 then we have found the second parenthesis so increment i by one to find the first parenthesis since brackets may contain more than two open parentheses
		i++;
	}	
	if(i == 0){ //check if there was no open parantheses in brackets, if yes
		int q=k;//keep counter and reset it as brackets has one open parenthesis only.
	    for (j = 1; j < brackets.length()-2; ++j) {
	    	if(brackets[j]== '(' && k!=q){ //check the first parenthesis if it is closed and find the second open parenthesis in brackets string
	        q=0;//reset counter
	      }
	    }
	}//when no open parentheses are found then k should not be changed so just reset it. 
	if(k!=q){ //if the first and last parentheses were closed
		if (k == brackets[j+1]== ')'){
			return true; //finding the opening parenthesis
		}else{ //we did not find any open parantheses, then return false