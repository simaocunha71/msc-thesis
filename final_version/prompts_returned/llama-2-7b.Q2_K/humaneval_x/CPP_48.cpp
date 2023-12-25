/*
Checks if given string is a palindrome
>>> is_palindrome("")
true
>>> is_palindrome("aba")
true
>>> is_palindrome("aaaaa")
true
>>> is_palindrome("zbcd")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_palindrome(string text){
	int n=text.size();
	for (int i=0,j=n-1;i<n;++i,--j) 
	if (text[i]!=text[j]) return false;
	return true;
}

int main(){
	string text="a";
	printf("The palindrome is '%s'\n",text);
	return 0;
}