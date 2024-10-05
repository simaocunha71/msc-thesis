    string str(str.rbegin(),str.rend());
    while(!is_palindrome(str)){
        for(int i=0;i<str.size();i++)
            if(str[i]!=str[0])
                str=str.substr(i)+str.substr(0,i);
    }
    return str;
}

int main() {
    string str="cata";
    printf("%s\n",make_palindrome(str).c_str());
    return 0;
}


#include <iostream>

using namespace std;

int main() {
    string str = "cata";
    cout << make_palindrome(str) << endl;
    return 0;
}


#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;
bool is_palindrome(string str){
    //Test if given string is a palindrome
    string s(str.rbegin(),str.rend());
    return s==str;
}
string make_palindrome(string str){
    /*
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome("")
    ""
    >>> make_palindrome("cat")
    "catac"
    >>> make_palindrome("cata")
    "catac"
    */

    string str(str.rbegin(),str.rend());
    while(!is_palindrome(str)){
        for(int i=0;i<str.size();i++)
            if(str[i]!=str[0])
                str=str.substr(i)+str.substr(0,i);
    }
    return str;
}

int main() {
    string str="cata";
    printf("%s\n",make_palindrome(str).c_str());
    return 0;
