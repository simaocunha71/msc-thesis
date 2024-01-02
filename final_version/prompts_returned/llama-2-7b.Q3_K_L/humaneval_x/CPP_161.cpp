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
	int len=s.length();
	for (int i=len-1;i>=0 ;i--) {
		if ('a'<=s[i]&&s[i]<='z')
			s[i]+=32;
		else if ('A'<=s[i]&&s[i]<='Z')
			s[i]-=32;
	}
	return s;
}
int main(void){
	string s="1234";
	printf("resulted %s\n",solve(s));
	return 0;
}