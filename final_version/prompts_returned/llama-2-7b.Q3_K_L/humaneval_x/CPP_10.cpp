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
    
    //find the longest postfix of supplied string that is a palindromic:
    int max_len=1;
    for (int i=0;i<str.size();++i){
        if(is_palindrome(str.substr(max_len,str.size()-max_len))&&(max_len+i<=str.size())){//check if the substring is a palindrome and its length > max length of found string
            max_len=max_len+i;
        }
    } 
    
    //append to the end of the string reverse of a string prefix that comes before the palindromic suffix:
    char temp[max_len];
    for (int i=0;i<str.size();++i){
        if(is_palindrome(str.substr(max_len-1,str.size()-max_len))&&(max_len>i+1)){//check if the substring is a palindrome and its length > max length of found string
            str[max_len-2]=temp[i];
        }
    } 
    
    return str;  
}
int main(){
    int n=0,l=32767;
    string input="cat",s=make_palindrome(input);
    