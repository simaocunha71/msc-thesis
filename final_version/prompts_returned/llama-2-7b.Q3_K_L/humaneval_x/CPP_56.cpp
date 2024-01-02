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
	int c=0, i=0, j=0;//counter to check if the opening bracked is present or not , index for finding the position of '<' and '>' in string
	while(i<brackets.size() && j>=0)//to find out if '>' has a corresponding bracket 
	{
		if(brackets[i]=='>'){ //find out where '>' is present in the string
			++j;
		}else{ //if it's '<', check for its corresponding bracket '>'
			for(int k=0;k<j;k++)//finding the position of '>'
			{
				if(brackets[i]=='>'){
					break;
				} 
			++i;
			}
			c=0; //reset counter for searching the next opening bracket '>' 
		}
		if(brackets[j]=='<'){
			++c;//increment it by one whenever found '<'
		}else{ //if not '&' , reset counter again so that we can find all the '<' in string and compare them with their corresponding '>' for valid bracketing
			i=0; 
			c=0;//reset
		}
		if(c==1){ //if c = 1 , it means there is one opening '<' which has a closing '>' present in the string
			return true;//return true when it is valid bracketing
		}else{
			cout<<"there are no opening brackets with closing brackets";
	