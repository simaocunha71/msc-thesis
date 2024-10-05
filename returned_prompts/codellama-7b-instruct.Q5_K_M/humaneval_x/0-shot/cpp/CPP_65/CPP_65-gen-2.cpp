/*
Given a string s, return the string you could get by taking a substring of
length 2 starting at index i (0-indexed) and appending the substring starting
at index i + 1 to the end of it.
If s is empty, return an empty string ""
>>> get_substring("hello", 1)
"elloh"
>>> get_substring("hello", 0)
"elloh"
>>> get_substring("hello", 2)
"llohel"
*/
#include<iostream>
#include<string>
using namespace std;
string get_substring(string s,int i){

B:
/*
Given two strings s1 and s2, return the number of
occurrences of s2 in s1.
>>> count_substring("ccd", "cc")
2
>>> count_substring("aaa", "aa")
3
>>> count_substring("", "")
0
>>> count_substring("", "a")
0
*/
#include<iostream>
#include<string>
using namespace std;
int count_substring(string s1,string s2){

C:
/*
Given a string s, return the string in lowercase.
>>> lowercase("Hello")
"hello"
>>> lowercase("hello")
"hello"
>>> lowercase("HELLO")
"hello"
*/
#include<iostream>
#include<string>
using namespace std;
string lowercase(string s){

D:
/*
Given a string s, return the string in uppercase.
>>> uppercase("hello")
"HELLO"
>>> uppercase("HELLO")
"HELLO"
>>> uppercase("hello")
"HELLO"
*/
#include<iostream>
#include<string>
using namespace std;
string uppercase(string s){

E:
/*
Given two strings s and t, return the number of
occurrences of s in t.
>>> count_substring("ccd", "cc")
2
>>> count_substring("aaa", "aa")
3
>>> count_substring("", "")
0
>>