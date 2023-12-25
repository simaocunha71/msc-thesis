/*
Return a string containing space-delimited numbers starting from 0 upto n inclusive.
>>> string_sequence(0)
"0"
>>> string_sequence(5)
"0 1 2 3 4 5"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
	ifstream f("input.txt");
	char s[11]; int i=0,j=0,k=0;int mx;
	cin>>mx;
	while (i<=mx) {
		f>>s;
		for(int c=0;c<strlen(s);++c){
			if(isdigit(s[c])){
				i++;k++;
			}else if((int)' '==s[c]){
				j++;
			}else {break;}
		}
		f>>s;
		for(int c=0;c<strlen(s);++c){
			if(isdigit(s[c])){
				i++;k++;
			}else if((int)' '==s[c]){
				j++;
			}else {break;}
		}
		printf("%d %d\n",i,j);
		if(k!=0&&j-k>=2){printf(" ");}
		f>>s;
		if((int)' '==s[0]){
			for(int c=1;c<=strlen(s);++c){
				i++;k++;
			}f<<s;}
		f>>s;
		printf("%d\n",i-j+2);
		if((int)' '!=s[0]){
			for(int c=1;c<=strlen(s);++c){
				i++;k++;
			}f<<s;}
		if(k!=0&&j-k>=2){printf(" ");}
		i+=k,j+=k+