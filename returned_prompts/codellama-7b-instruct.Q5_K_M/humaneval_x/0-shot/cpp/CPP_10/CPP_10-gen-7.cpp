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
    string::iterator it=str.begin();
    string::iterator last=str.end()-1;
    while(it!=last){
        if(!is_palindrome(string(it,last))){
            string::iterator first=str.begin();
            string::iterator mid=it;
            string::iterator last=str.end()-1;
            while(mid!=last){
                if(is_palindrome(string(first,mid))){
                    break;
                }
                mid++;
            }
            str=string(first,mid)+string(mid,last)+string(mid,mid+1);
            break;
        }
        last--;
    }
    return str;
}
int main(){
    string s;
    cin>>s;
    cout<<make_palindrome(s)<<endl;
    return 0;
}

