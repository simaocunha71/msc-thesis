    int i,n,l,r;
    n = text.length();
    for(i=0;i<n;i++)
    {
        if(i<n-i-1)
        {
            l = text[i];
            r = text[n-i-1];
            if(l!=r)
                return false;
        }
        else
            break;
    }
    return true;
}






ANSWER:
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
bool is_palindrome(string text){

    int i,n,l,r;
    n = text.length();
    for(i=0;i<n;i++)
    {
        if(i<n-i-1)
        {
            l = text[i];
            r = text[n-i-1];
            if(l!=r)
                return false;
        }
        else
            break;
    }
    return true;
}



































































































































































































