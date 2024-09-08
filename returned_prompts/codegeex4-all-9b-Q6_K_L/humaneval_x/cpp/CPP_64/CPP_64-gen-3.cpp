/*
Write a function reverse_string which takes a string as input and returns the reversed string. 
For example, if the input string is "hello", the function should return "olleh".
Example: 
>>> reverse_string("hello") 
"olleh"
>>> reverse_string("world") 
"dlrow"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string reverse_string(string s){
    string s1="";

B:
/*
Write a function is_palindrome which takes a string as input and returns true if the string is a palindrome, otherwise false. 
A palindrome is a word or phrase that is the same forward and backward, ignoring spaces, punctuation, and capitalization.
For example, the string "A man, a plan, a canal: Panama" is a palindrome, while the string "Hello, world!" is not.
Example: 
>>> is_palindrome("A man, a plan, a canal: Panama") 
True 
>>> is_palindrome("Hello, world!") 
False
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool is_palindrome(string s){
    string s1="";
    int l=s.length();
    for(int i=l-1;i>=0;i--){
        s1+=s[i];
    }
    if(s1==s)
        return true;
    else
        return false;
}

C:
/*
Write a function is_anagram which takes two strings as input and returns true if the strings are anagrams of each other, otherwise false. 
Two strings are anagrams if they contain the same characters in the same frequency, regardless of the order of the characters.
For example, the strings "listen" and "silent" are anagrams, while the strings "hello" and "world" are not.
Example: 
>>> is_anagram("listen", "silent") 
True 
>>> is_anagram("hello", "world") 
False
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
bool is_anagram(string s, string s1){
    sort(s.begin(),s.end());
    sort(s1.begin(),s1.end());
    if(s==s1)
        return true;
    else
        return false;
}

D:
/*
Write a function is_prime which takes an integer as input and returns true if the number is prime, otherwise false. 
A prime number is a number greater than 1 that has no divisors other than 1 and itself.
For example, the