/*
Write a function that takes a message, and encodes in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the english alphabet. 
Assume only letters. 

Examples:
>>> encode('test")
"TGST"
>>> encode("This is a message")
'tHKS KS C MGSSCGG"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){
	int n=message.size();
	string res="";
	res+='a';
	for (int i = 0 ; i < n-1; ++i) {
		if ('a' <= message[i] && message[i] <= 'z')
			message[i]+=26*(char)('z'-'a');
		else if ('A' <= message[i] && message[i] <= 'Z')
			message[i]-=(char)('z'-'A');
	}
	if(message.back()==32){
		res+='a';
		int cnt=0;
		for (int i = 1 ; i < n-1; ++i) {
			cnt+=((message[i]-'A') * (double)(32.0));
		}
		res+=(char)'a'+ (char)((double)cnt/(32.0 - 'z' + 'A'));
	} else res+= message[n-1];
	return res;
}