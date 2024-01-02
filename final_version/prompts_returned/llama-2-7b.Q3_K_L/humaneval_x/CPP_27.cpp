/*
For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case("Hello")
"hELLO"
*/
#include<stdio.h>
#include<string>
using namespace std;
string filp_case(string str){
	int len=str.length();
	for (int i = 0;i<len;i++){
		if ('a' <= str[i] && str[i]<= 'z'){
			str[i]+='A';
		}else if('Z' <= str[i] && str[i] <= 'Z'){
			str[i]+='z';
		}

	}
	return  str;
}
int main(){
	string s="Hello";
	filp_case(s);
}
