/*
You are given a string s.
if s[i] is a letter, reverse its case from lower to upper or vise versa, 
otherwise keep it as it is.
If the string contains no letters, reverse the string.
The function should return the resulted string.
Examples
solve("1234") = "4321"
solve("ab") = "AB"
solve("#a@C") = "#A@c"
*/
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
	int i=0,j=s.length()-1;//start reverse at last index of string
	int temp='z'+52;
	while((i<j)&&(s[i]!=' ')){
		if(!isalpha(s[i])){// not alphabetic,return the original string
			printf("not alphabet\n");
			printf("%c",s[i]);
			return s;
		}
		else if(islower(s[i])){// if lowercase letter,
			while(!isalpha(s[++i])&&i<j){// find the first alphabetic character and reverse it
				printf("%c",s[i]);
			}s[i]='a'+1;
			for(int k=i+2;k<=j-1;k++){// if this is not first letter, 
				if(!isalpha(s[k])&&!ispunctuation(s[k])){
					while((int)(k<i)&&isalnum(s[k])){// find the next alphabetic character and reverse it
						printf(" %c",s[k]);
						k++;
					}
				if(!isalpha(s[k])){ 
					while((int)(k<j)&&isalnum(s[k])&&!ispunctuation(s[k])&&temp!=s[k]-'a'+52){//