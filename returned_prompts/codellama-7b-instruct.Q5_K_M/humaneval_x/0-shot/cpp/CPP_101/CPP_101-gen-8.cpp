/*
Write a function that takes a string as a parameter and returns the string
with all the vowels removed.

For example:
no_vowels("hello") == "hll"
no_vowels("aeiou") == ""
no_vowels("aeiou") == ""
*/
#include<stdio.h>
#include<string>
using namespace std;
string no_vowels(string s){

B:
/*
Write a function that takes a vector of integers as a parameter and returns
the sum of the elements in the vector.

For example:
sum_vector({1, 2, 3}) == 6
sum_vector({4, 5, 6}) == 15
*/
#include<stdio.h>
#include<vector>
using namespace std;
int sum_vector(vector<int> v){

C:
/*
Write a function that takes a string as a parameter and returns a vector of
strings where each string is a word in the original string.

For example:
words_string("Hello, world!") == {"Hello", "world"}
words_string("") == {}
*/
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
vector<string> words_string(string s){

D:
/*
Write a function that takes a vector of integers as a parameter and returns
a vector of pairs of integers where the first element in each pair is the
index of the first occurrence of the integer in the vector and the second
element is the index of the last occurrence of the integer in the vector.

For example:
indexes({1, 2, 3, 2, 1}) == {{0, 4}, {1, 3}, {2, 4}}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<pair<int, int> indexes(vector<int> v){

E:
/*
Write a function that takes a vector of integers as a parameter and returns
the number of times that the integer 1 appears in the vector.

For example:
count_ones({1, 2, 3, 2