/*
Given a map, return true if all keys are strings in lower 
case or all keys are strings in upper case, else return false.
The function should return false is the given map is empty.
Examples:
check_dict_case({{"a","apple"}, {"b","banana"}}) should return true.
check_dict_case({{"a","apple"}, {"A","banana"}, {"B","banana"}}) should return false.
check_dict_case({{"a","apple"}, {"8","banana"}, {"a","apple"}}) should return false.
check_dict_case({{"Name","John"}, {"Age","36"}, {"City","Houston"}}) should return false.
check_dict_case({{"STATE","NC"}, {"ZIP","12345"} }) should return true.
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
bool check_dict_case(map<string,string> dict){

    if(dict.empty()){
        return false;
    }
    bool lower = false;
    bool upper = false;
    for(auto it = dict.begin(); it != dict.end(); it++){
        if(it->first[0] >= 'a' && it->first[0] <= 'z'){
            lower = true;
        }
        if(it->first[0] >= 'A' && it->first[0] <= 'Z'){
            upper = true;
        }
    }
    if(lower && upper){
        return false;
    }
    return true;
<|code_middle|>
}
