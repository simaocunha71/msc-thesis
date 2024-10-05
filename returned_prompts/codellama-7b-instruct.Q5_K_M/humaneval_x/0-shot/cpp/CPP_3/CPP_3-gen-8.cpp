/*
Write a function that takes in a string of round, curly, and square open and closing brackets
and checks whether the order in which they are nested is valid. For example, given the input
string "()([]){}", the function should return true since the order of nesting is valid.

On the other hand, given the input string "()([)]{}", the function should return false since
the nesting is invalid due to the closing square bracket "]" appearing before the corresponding
opening square bracket "(".

>>> is_valid_nesting("()([]){}")
true
>>> is_valid_nesting("()([)]{}")
false
*/
#include <iostream>
#include <string>
using namespace std;
bool is_valid_nesting(string s){

