    int len = str.length();
    if(len==0 || is_palindrome(str)){
        return str;
    }
    string rev(str.rbegin(),str.rend());
    string pre(str.begin(),str.begin()+1);
    string suf(str.begin()+1,str.end());
    while(!is_palindrome(pre)){
        pre = string(str.begin(),str.begin()+pre.length()-1);
    }
    suf = string(str.begin()+pre.length(),str.end());
    string add = rev.substr(0,len-pre.length());
    return str+add;
}

int main(){
    printf("%s\n", make_palindrome("").c_str());
    printf("%s\n", make_palindrome("cat").c_str());
    printf("%s\n", make_palindrome("cata").c_str());
    return 0;
}

*/

//src/main.cpp
#include<stdio.h>
#include<string>
using namespace std;
bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}
string make_palindrome(string str){
    int len = str.length();
    if(len==0 || is_palindrome(str)){
        return str;
    }
    string rev(str.rbegin(),str.rend());
    string pre(str.begin(),str.begin()+1);
    string suf(str.begin()+1,str.end());
    while(!is_palindrome(pre)){
        pre = string(str.begin(),str.begin()+pre.length()-1);
    }
    suf = string(str.begin()+pre.length(),str.end());
    string add = rev.substr(0,len-pre.length());
    return str+add;
}

int main(){
    printf("%s\n", make_palindrome("").c_str());
    printf("%s\n", make_palindrome("