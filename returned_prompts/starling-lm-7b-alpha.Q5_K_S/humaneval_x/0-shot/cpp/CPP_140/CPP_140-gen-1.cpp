#include<stdio.h>
#include<string>
using namespace std;
string fix_spaces(string text){
	for(int i=0;i<text.length();i++){
		if(text[i]==' ')
			text[i]='_';
	}
	for(int i=2;i<text.length();i++){
		if(text[i]==' ' && text[i-1]==' ' && text[i-2]==' '){
			text[i]='-';
		}
	}
	return text;
}