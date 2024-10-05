#include<stdio.h>
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
    //Find the longest postfix of supplied string that is a palindrome
    string s(str.rbegin(),str.rend());
    int l=s.size();
    int i;
    for(i=0;i<l;i++){
        if(!is_palindrome(s.substr(0,i+1))){
            break;
        }
    }
    //Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    string pref(str.begin(),str.begin()+i);
    string suf(s.begin(),s.begin()+i);
    string r(pref.rbegin(),pref.rend());
    return str+r+suf;
}
int main(){
    string s;
    cin>>s;
    cout<<make_palindrome(s)<<endl;
    return 0;
}
