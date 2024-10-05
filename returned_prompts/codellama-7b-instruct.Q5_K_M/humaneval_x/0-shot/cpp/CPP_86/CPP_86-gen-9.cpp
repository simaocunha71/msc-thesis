/*
Write a function that takes a string and returns a string where all the words
have the first and last characters swapped.
For example:
anti_shuffle("Hello World") returns "Hlllo Wrld"
*/
#include<stdio.h>
#include<string>
using namespace std;
string anti_shuffle(string s){

B:
/*
Write a function that takes a string and returns the number of times
a substring appears in the string.
For example:
count_substring("catcowcat", "cat") returns 2
*/
#include<stdio.h>
#include<string>
using namespace std;
int count_substring(string str, string substr){

C:
/*
Write a function that takes two strings and returns a boolean
indicating whether one string is a rotation of the other.
For example:
is_rotation("hello", "lohel") returns true
is_rotation("hello", "lohelx") returns false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_rotation(string s1, string s2){

D:
/*
Write a function that takes a string and returns a string where all the
occurences of space, tab, and newline are replaced by the %20.
For example:
urlify("Hello World") returns "Hello%20World"
*/
#include<stdio.h>
#include<string>
using namespace std;
string urlify(string s){

E:
/*
Write a function that takes a string and returns a string where all the
occurences of %20 are replaced by space, tab, and newline.
For example:
urlify2("Hello%20World") returns "Hello World"
*/
#include<stdio.h>
#include<string>
using namespace std;
string urlify2(string s){

F:
/*
Write a function that takes a string and returns the number of words it
contains. A word is defined as a contiguous sequence of non-space
characters.
For example:
num_words("Hello World") returns 2
num_words("Hello   World") returns 2
num_words("