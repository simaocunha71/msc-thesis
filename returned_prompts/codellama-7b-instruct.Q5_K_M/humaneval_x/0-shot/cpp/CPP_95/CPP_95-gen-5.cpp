/*
Given a map and a key, return true if the key is in the map 
and its value is in lower case, else return false.
Examples:
check_key_lowercase({{"a","apple"}, {"b","banana"}}, "a") should return true.
check_key_lowercase({{"a","apple"}, {"b","banana"}}, "A") should return false.
check_key_lowercase({{"a","apple"}, {"b","banana"}}, "B") should return false.
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
bool check_key_lowercase(map<string,string> dict, string key){

B:
/*
Given a map, return true if all values are strings in lower 
case, else return false.
Examples:
check_map_lowercase({{"a","apple"}, {"b","banana"}}) should return true.
check_map_lowercase({{"a","apple"}, {"A","banana"}, {"B","banana"}}) should return false.
check_map_lowercase({{"a","apple"}, {"8","banana"}, {"a","apple"}}) should return false.
check_map_lowercase({{"Name","John"}, {"Age","36"}, {"City","Houston"}}) should return false.
check_map_lowercase({{"STATE","NC"}, {"ZIP","12345"} }) should return false.
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
bool check_map_lowercase(map<string,string> dict){

C:
/*
Given a map, return true if all values are strings in upper 
case, else return false.
Examples:
check_map_uppercase({{"A","APPLE"}, {"B","BANANA"}}) should return true.
check_map_uppercase({{"a","apple"}, {"A","banana"}, {"B","banana"}}) should return false.
check_map_uppercase({{"a","apple"}, {"8","banana"}, {"a","apple"}}) should return false.
check_map_uppercase({{"