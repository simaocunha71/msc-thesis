/*
Task
We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
then check if the result string is palindrome.
A string is called palindrome if it reads the same backward as forward.
You should return a vector containing the result string and "True"/"False" for the check.
Example
For s = "abcde", c = "ae", the result should be ("bcd","False")
For s = "abcdef", c = "b"  the result should be ("acdef","False")
For s = "abcdedcba", c = "ab", the result should be ("cdedc","True")
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
	int j=0;
	for(int i=1;i<=c.size();i++){
		j++;
		if(!s[j-1].compare(c[i])){
			s[j-1]='\0';
		}
		else if(s[j-1]){
			printf("true");
			return s;
		}
		else
			return s;
	}
	if(!s) return s;
	int i=0;
	for(i=0;i<=s.size();i++){
		if(j==1){
			printf("true");
			return s;
		}
		else if(s[i].compare(c[j])){
			s[j-2]='\0';
		}
		else if(s[i]){
			printf("true");
			return s;
		}
	}

	int k=1;
	for(k=1;k<=c.size();k++){
		if(!s[k-1].compare(c[k])) {
			continue;
		}
		else{
			printf("true");
	