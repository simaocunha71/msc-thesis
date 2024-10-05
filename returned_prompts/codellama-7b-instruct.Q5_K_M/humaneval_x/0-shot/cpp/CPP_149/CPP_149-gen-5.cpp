/*
Write a function that accepts a string and a character as parameters,
and returns the string after replacing all the occurrences of the character with the given string,
For example:
assert replace_all("abcd", "d", "c") => "abc"
assert replace_all("abcd", "b", "c") => "acd"
*/
#include<stdio.h>
#include<string>
using namespace std;
string replace_all(string str, char ch, string new_str){
B:
/*
Write a function that accepts a vector of integers as a parameter,
and returns the sum of all the elements in the vector.
For example:
assert sum({1, 2, 3, 4, 5}) => 15
*/
#include<stdio.h>
#include<vector>
using namespace std;
int sum(vector<int> v){
C:
/*
Write a function that accepts a vector of strings and a string as parameters,
and returns the vector after adding the given string to it,
For example:
assert vector_add({"a", "b"}, "c") => {"a", "b", "c"}
assert vector_add({"a", "b"}, "") => {"a", "b"}
*/
#include<stdio.h>
#include<string>
#include<vector>
using namespace std;
vector<string> vector_add(vector<string> v, string s){
D:
/*
Write a function that accepts a vector of integers and a number as parameters,
and returns the vector after adding the given number to it,
For example:
assert vector_add({1, 2, 3}, 4) => {5, 6, 7}
assert vector_add({1, 2, 3}, 0) => {1, 2, 3}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> vector_add(vector<int> v, int n){
E:
/*
Write a function that accepts a vector of integers as a parameter,
and returns the sum of all the elements in the vector,
For example:
assert sum({1, 2, 3, 