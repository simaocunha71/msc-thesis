#include<iostream>
#include<string>
#include<algorithm>
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
    if(is_palindrome(str)) return str;
    int i=0,j=0;
    for(i=str.length()-1;i>=0;i--){
        if(is_palindrome(str.substr(0,i+1))) break;
    }
    string s1(str,0,i+1);
    string s2(str,i+1,str.length()-i-1);
    reverse(s2.begin(),s2.end());
    return s1+s2;
}
int main(){
    string str;
    cin>>str;
    cout<<make_palindrome(str)<<endl;
}
