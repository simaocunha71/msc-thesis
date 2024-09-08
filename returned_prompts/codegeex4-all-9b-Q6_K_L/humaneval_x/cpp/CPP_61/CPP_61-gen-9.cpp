/*
Write a function that, given a string, returns whether all parentheses in the string are balanced.
A string of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis.

>>> balanced_parens("")
true
>>> balanced_parens("(")
false
>>> balanced_parens("()")
true
>>> balanced_parens("()()")
true
>>> balanced_parens("(())")
true
>>> balanced_parens("(()")
false
>>> balanced_parens(")()")
false
>>> balanced_parens("(()()")
false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool balanced_parens(string parens){

B:
/*
Write a function that takes an array of words and returns the length of the longest word.

>>> longest_word(["short", "really, really long word", "medium"])
'really, really long word'
*/
#include<stdio.h>
#include<string>
using namespace std;
string longest_word(vector<string> words){

C:
/*
Write a function that takes a string and returns a string in which all characters are repeated once.

>>> double_characters("String")
'Sttrinng'
>>> double_characters("Hello world!")
'Hellollo woorld!!'
>>> double_characters("")
''
*/
#include<stdio.h>
#include<string>
using namespace std;
string double_characters(string input_string){

D:
/*
Write a function that takes a string and returns the number of characters in the string that are not whitespace characters.

>>> count_characters("String")
6
>>> count_characters("Hello world!")
12
>>> count_characters("")
0
*/
#include<stdio.h>
#include<string>
using namespace std;
int count_characters(string input_string){
