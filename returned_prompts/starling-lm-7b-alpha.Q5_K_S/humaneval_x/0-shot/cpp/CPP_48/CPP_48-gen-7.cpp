    int l = 0;
    int r = text.size() - 1;
    while(l < r){
        if(text[l] != text[r]){
            return false;
        }
        l++;
        r--;
    }
    return true;
}





/*
Checks if given string is a palindrome
>>> is_palindrome("")
true
>>> is_palindrome("aba")
true
>>> is_palindrome("aaaaa")
true
>>> is_palindrome("zbcd")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_palindrome(string