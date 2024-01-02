/*
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
	int max = 0, min = 256-1 ,i=0,j=0,k=0; //max will store the highest digit and min will store lowest digit
	for (int i=0; i<s.length();i++){
		//If it is alphanumeric character then increment k else increment j
		if((s[i]>=96 && s[i]<=123) || (s[i]>=48 && s[i] <=57)){
			k++;
		}
		else{
			j++;
		}
	}
	string ans;
	for(int i=0;i<s.length();i++){
		if((s[i]>=96 && s[i]<=123) || (s[i]>=48 && s[i] <=57)){
			ans += to_string(max);
		}
		else{ //If current character is not alphanumeric then store it in ans and increment the j count
			ans+=to_string(j+1);
			j++;
		}
		if((s[i]>=96 && s[i]<=123) || (s[i]>=48 && s[i] <=57)){ //If current char is alphanumeric
			max=min;
			ans += to_string(j); // Store the current character's count in ans