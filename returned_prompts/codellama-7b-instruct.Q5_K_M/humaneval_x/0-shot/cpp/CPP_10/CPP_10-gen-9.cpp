#include<stdio.h>
#include<string>
using namespace std;
bool is_palindrome(string str){
    //Test if given string is a palindrome 
    string s(str.rbegin(),str.rend());
    return s==str;
}
string make_palindrome(string str){
    /*
    Find the shortest palindrome that begins with a supplied string. 
    Algorithm idea is simple: - Find the longest postfix of supplied string that is a palindrome. 
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome("") 
    "" 
    >>> make_palindrome("cat") 
    "catac" 
    >>> make_palindrome("cata") 
    "catac" 
    */
    if(is_palindrome(str))return str;
    int i=str.size()-1;
    while(i>=0 && !is_palindrome(str.substr(0,i+1))){
        i--;
    }
    string s(str.rbegin(),str.rbegin()+i);
    return str+s;
}
int main(){
    string s;
    cin>>s;
    string t=make_palindrome(s);
    printf("%s",t.c_str());
    return 0;
}
