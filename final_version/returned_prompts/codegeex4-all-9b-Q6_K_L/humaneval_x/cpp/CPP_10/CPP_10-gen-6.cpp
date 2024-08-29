#include<iostream>
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

    if(is_palindrome(str)){
        return str;
    }

    for(int i=str.length()-1;i>=0;i--){
        if(is_palindrome(str.substr(i,str.length()-i))){
            string s=str.substr(0,i);
            string r(s.rbegin(),s.rend());
            return str+r;
        }
    }
}

int main(){
    cout<<make_palindrome("cat")<<endl;
    cout<<make_palindrome("cata")<<endl;
    cout<<make_palindrome("cataca")<<endl;
    return 0;
}
