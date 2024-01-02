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
	int start=0,end=text.size()-1;
	if (end<=start) return false;
	while (!isalpha(text[start++])) {}
	while ((start>=0)&&(!isalpha(text[--end]))) {}
	return text==string(start+1,end); //text.substr(0,end-1)=text.substr(end+1,-1).swap(text);
}
int main(){
	printf("%s is palindrome\n",is_palindrome("").c_str());
	printf("%s is not a palindrome\n",is_palindrome("zbcd").c_str());
	return 0;
}
