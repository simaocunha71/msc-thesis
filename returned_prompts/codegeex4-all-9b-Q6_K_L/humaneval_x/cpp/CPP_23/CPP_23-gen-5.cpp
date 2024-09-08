/*
Return sum of all chars in given string
>>> sumstr("")
0
>>> sumstr("abc")
300
>>> sumstr("12345")
150
*/
#include<stdio.h>
#include<string>
using namespace std;
int sumstr(string str){

B:
/*
Return first char of given string
>>> firstchar("")
' '
>>> firstchar("abc")
'a'
>>> firstchar("12345")
'1'
*/
#include<stdio.h>
#include<string>
using namespace std;
char firstchar(string str){

C:
/*
Return last char of given string
>>> lastchar("")
' '
>>> lastchar("abc")
'c'
>>> lastchar("12345")
'5'
*/
#include<stdio.h>
#include<string>
using namespace std;
char lastchar(string str){

D:
/*
Return index of given char in given string
>>> find("a","abc")
1
>>> find("b","abc")
2
>>> find("c","abc")
3
>>> find("d","abc")
-1
*/
#include<stdio.h>
#include<string>
using namespace std;
int find(char ch,string str){

E:
/*
Return index of given char in given string from given index
>>> find("a","abc",1)
-1
>>> find("b","abc",1)
2
>>> find("c","abc",1)
-1
>>> find("d","abc",1)
-1
*/
#include<stdio.h>
#include<string>
using namespace std;
int find(char ch,string str,int index){

F:
/*
Return true if given string is empty,else false
>>> isEmpty("")
true
>>> isEmpty("abc")
false
>>> isEmpty("12345")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool isEmpty(string str){

G:
/*
Return true if given string is not empty,else false
>>> isNotEmpty("")
false
>>> isNotEmpty("abc")
true
>>> isNotEmpty("12345")
true
*/
#include<stdio.h>
#include<string>
using namespace std;
bool isNotEmpty(string str){

H:
/*
Return true if given string is palindrome,else false
>>> isPalindrome("")
true
>>> isPalindrome("abcba")
true
>>> isPalindrome("abc")
false
>>> isPalindrome("12345")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool isPalindrome(string str){

I:
/*
Return true if given string is not palindrome,else false
>>> isNotPalindrome("")
false
>>> isNotPalindrome("abcba")
false
>>> is