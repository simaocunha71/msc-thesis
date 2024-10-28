/*
Write a function that takes a string and returns a vector of strings,
where each string is a possible word that can be formed by rearranging the letters of the original string.
For example:
assert rearrange("abc") => {"abc", "bca", "cab"}
assert rearrange("aabb") => {"aabb", "abab", "baba", "bbaa"}
assert rearrange("hello") => {"hello", "helo", "helo", "heol", "hlel", "lhel", "lheo", "leah", "lehl", "lhea", "leha", "lehl", "lhea", "lehl", "lhea", "lehl", "lhea", "lehl"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> rearrange(string s){

C:
/*
Write a function that takes a vector of strings and returns the number of uniqe strings in the vector.
For example:
assert unique_strings({"a", "b", "c", "c"}) => 3
assert unique_strings({"a", "a", "a"}) => 1
assert unique_strings({"a", "b", "c", "d"}) => 4
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int unique_strings(vector<string> v){

D:
/*
Write a function that takes a vector of integers and returns the number of uniqe integers in the vector.
For example:
assert unique_integers({1, 2, 3, 3}) => 3
assert unique_integers({1, 1, 1}) => 1
assert unique_integers({1, 2, 3, 4}) => 4
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int unique_integers(vector<int> v){

E:
/*
Write a function that takes a vector