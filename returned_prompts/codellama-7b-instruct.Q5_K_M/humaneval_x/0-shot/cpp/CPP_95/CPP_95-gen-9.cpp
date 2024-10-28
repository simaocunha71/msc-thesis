/*
Given a map, return true if all keys are strings in lower 
case or all keys are strings in upper case, else return false.
The function should return false is the given map is empty.
Examples:
check_map_case({{"a","apple"}, {"b","banana"}}) should return true.
check_map_case({{"a","apple"}, {"A","banana"}, {"B","banana"}}) should return false.
check_map_case({{"a","apple"}, {"8","banana"}, {"a","apple"}}) should return false.
check_map_case({{"Name","John"}, {"Age","36"}, {"City","Houston"}}) should return false.
check_map_case({{"STATE","NC"}, {"ZIP","12345"} }) should return true.
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
bool check_dict_case(map<string,string> dict){

    if(dict.empty())
        return false;
    bool lower_case = true;
    bool upper_case = true;
    for(auto i : dict){
        if(!islower(i.first[0]) && !isupper(i.first[0]))
            lower_case = false;
        if(!islower(i.first[0]) && isupper(i.first[0]))
            upper_case = false;
        if(!lower_case && !upper_case)
            break;
    }
    return lower_case || upper_case;
}

int main(){
    map<string, string> mp;
    mp = {{"a","apple"}, {"b","banana"}};
    cout<<check_dict_case(mp)<<endl;
    mp = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    cout<<check_dict_case(mp)<<endl;
    mp = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    cout<<check_dict_case(mp)<<endl;
    mp = {{"Name","John"}, {"Age","36"}, {"City","Hou