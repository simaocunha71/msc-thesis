/*
Given a string s and a non-negative integer k, 
write a function to check if the last k characters 
of the string are spaces 

is_last_k_spaces("   ", 1) == true
is_last_k_spaces("   ", 3) == false
is_last_k_spaces(" a", 0) == false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_last_k_spaces(string s, int k){

B:
/*
Given a string s and a non-negative integer k, 
write a function to check if the first k characters 
of the string are spaces 

is_first_k_spaces("   ", 1) == true
is_first_k_spaces("   ", 3) == false
is_first_k_spaces(" a", 0) == false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_first_k_spaces(string s, int k){

C:
/*
Given a string s and a non-negative integer k, 
write a function to check if the first k characters 
of the string are spaces, and if so, remove them 

fix_first_k_spaces("   a", 1) == "a"
fix_first_k_spaces("   a", 3) == "a"
fix_first_k_spaces(" a", 0) == " a"
*/
#include<stdio.h>
#include<string>
using namespace std;
string fix_first_k_spaces(string s, int k){

D:
/*
Given a string s and a non-negative integer k, 
write a function to check if the last k characters 
of the string are spaces, and if so, remove them 

fix_last_k_spaces("   a", 1) == "a"
fix_last_k_spaces("   a", 3) == "a"
fix_last_k_spaces(" a", 0) == " a"
*/
#include<stdio.h>
#include<string>
using namespace std