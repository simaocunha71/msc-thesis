/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == "xix"
>>> int_to_mini_roman(152) == "clii"
>>> int_to_mini_roman(426) == "cdxxvi"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int number){
    vector<pair<int,string>> roman_nums;
    roman_nums.push_back(make_pair(1000,"m"));
    roman_nums.push_back(make_pair(900,"cm"));
    roman_nums.push_back(make_pair(500,"d"));
    roman_nums.push_back(make_pair(400,"cd"));
    roman_nums.push_back(make_pair(100,"c"));
    roman_nums.push_back(make_pair(90,"xc"));
    roman_nums.push_back(make_pair(50,"l"));
    roman_nums.push_back(make_pair(40,"xl"));
    roman_nums.push_back(make_pair(10,"x"));
    roman_nums.push_back(make_pair(9,"ix"));
    roman_nums.push_back(make_pair(5,"v"));
    roman_nums.push_back(make_pair(4,"iv"));
    roman_nums.push_back(make_pair(1,"i"));

    string result;
    for (int i = 0; i < roman_nums.size(); i++) {
        while (number >= roman_nums[i].first) {
            result += roman_nums[i].second;
            number -= roman_nums[i].first;
        }
    }

    return result