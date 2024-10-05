/*
Return vector of all suffixes from longest to shortest of the input string
>>> all_suffixes("abc")
{"abc", "bc", "c"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> all_suffixes(string str){

B:
/*
Return the longest common prefix of all the strings in the input vector
>>> longest_common_prefix({"abc", "abcd", "abcde"})
"abc"
>>> longest_common_prefix({"a", "b"})
""
*/
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
string longest_common_prefix(vector<string> strs){

C:
/*
Return the longest common suffix of all the strings in the input vector
>>> longest_common_suffix({"abc", "abcd", "abcde"})
"cde"
>>> longest_common_suffix({"a", "b"})
""
*/
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
string longest_common_suffix(vector<string> strs){

D:
/*
Return the Hamming distance between two strings
>>> hamming_distance("abc", "abd")
1
*/
#include<stdio.h>
#include<string>
using namespace std;
int hamming_distance(string str1, string str2){

E:
/*
Return the Levenshtein distance between two strings
>>> levenshtein_distance("abc", "abd")
1
*/
#include<stdio.h>
#include<string>
using namespace std;
int levenshtein_distance(string str1, string str2){

F:
/*
Return true if the input string is a palindrome, false otherwise
>>> is_palindrome("racecar")
true
>>> is_palindrome("not a palindrome")
false
*/
#include<stdio.h>
#include<string>
using namespace