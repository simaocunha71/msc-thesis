/*
Given an input vector of strings, return a new vector of strings with all the duplicates removed.
>>> remove_duplicates({"a", "b", "c", "b", "a"})
{"a", "b", "c"}
>>> remove_duplicates({"a", "b", "c", "b", "c"})
{"a", "b", "c"}
>>> remove_duplicates({"a", "b", "c", "b", "c", "a"})
{"a", "b", "c"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<unordered_set>
using namespace std;
vector<string> remove_duplicates(vector<string> strings){

B:
/*
Implement a function that takes in a string and returns a string where all the vowels have been removed.
>>> remove_vowels("hello")
"hll"
>>> remove_vowels("aeiou")
""
>>> remove_vowels("The quick brown fox jumps over the lazy dog")
"Th qck brwn fx jmps vr th lzy dg"
*/
#include<stdio.h>
#include<string>
using namespace std;
string remove_vowels(string input){

C:
/*
Given two strings, implement a function that returns true if a is a rotated version of b.
>>> is_rotated("apple", "pleap")
True
>>> is_rotated("apple", "ple")
False
>>> is_rotated("apple", "bale")
False
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_rotated(string a, string b){

D:
/*
Implement a function that takes in a string and returns a string where each character is the product of the ascii value of that character and the index of that character in the string.
>>> product_ascii("hello")
"28412108111"
>>> product_ascii("")
""
*/
#include<stdio.h>
#