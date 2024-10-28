/*
Given a string, return the string where all appearances of "but" have been replaced by "butt".

but_replace has been defined for you.

>>> but_replace("but", "butt")
"butt"
>>> but_replace("butt", "butt")
"butt"
>>> but_replace("but", "note")
"notet"
>>> but_replace("but", "")
"but"
*/
#include<stdio.h>
#include<string>
using namespace std;
string but_replace(string, string);
string but_replace(string s, string new_s){
	int i;
	for(i = 0;i < s.length();i++){
		if(s.at(i) == 'b' && s.at(i + 1) == 'u' && s.at(i + 2) == 't'){
			s.replace(i, 3, new_s);
			i += new_s.length();
		}
	}
	return s;
}
string but_replace(string s, string new_s){
	int i;
	for(i = 0;i < s.length();i++){
		if(s.at(i) == 'b' && s.at(i + 1) == 'u' && s.at(i + 2) == 't'){
			s.replace(i, 3, new_s);
			i += new_s.length();
		}
	}
	return s;
}
string but_replace(string s, string new_s){
	int i;
	for(i = 0;i < s.length();i++){
		if(s.at(i) == 'b' && s.at(i + 1) == 'u' && s.at(i + 2) == 't'){
			s.replace(i, 3, new_s);
			i += new_s.length();
		}
	}
	return s;
}
string but_replace(string