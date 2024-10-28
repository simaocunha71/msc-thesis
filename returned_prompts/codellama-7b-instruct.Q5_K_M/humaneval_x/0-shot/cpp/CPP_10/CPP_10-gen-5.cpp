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
    int l=str.length();
    int i;
    for(i=0;i<l;i++){
        if(is_palindrome(str.substr(0,i+1))==true)
            break;
    }
    return str.substr(0,i+1)+string(str.rbegin(),str.rbegin()+i);
}
int main(){
    string str;
    cin>>str;
    cout<<str<<" "<<make_palindrome(str)<<endl;
    return 0;
}
