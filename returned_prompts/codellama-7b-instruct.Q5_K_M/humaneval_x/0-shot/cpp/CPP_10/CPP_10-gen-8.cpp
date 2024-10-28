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
    int l=str.length();
    string s="";
    for(int i=0;i<l;i++)
    {
        if(is_palindrome(str.substr(0,i)))
        {
            s=str.substr(0,i);
            break;
        }
    }
    if(s=="" || s==str)
        return str+"_";
    string r=str.substr(s.length(),str.length()-s.length());
    return s+r.substr(0,r.length()-1)+r.substr(r.length()-1,1);
}
int main()
{
    string str;
    cin>>str;
    cout<<make_palindrome(str);
    return 0;
}
