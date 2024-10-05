/*
Input is a space-delimited string of numberals from "zero" to "nine".
Valid choices are "zero", "one", 'two", 'three", "four", "five", 'six", 'seven", "eight" and "nine".
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five")
"one three five"
*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
string sort_numbers(string numbers){
    map<string, int> num_map;
    int num_count = 0;
    int num_index = 0;
    int num_min = 0;
    int num_max = 0;
    string sorted_nums = "";

    num_count = 0;
    num_index = 0;
    num_min = 0;
    num_max = 0;
    sorted_nums = "";

    num_count = 0;
    num_index = 0;
    num_min = 0;
    num_max = 0;
    sorted_nums = "";

    num_map["zero"] = 0;
    num_map["one"] = 1;
    num_map["two"] = 2;
    num_map["three"] = 3;
    num_map["four"] = 4;
    num_map["five"] = 5;
    num_map["six"] = 6;
    num_map["seven"] = 7;
    num_map["eight"] = 8;
    num_map["nine"] = 9;

    for(num_index = 0; num_index < numbers.size(); num_index++){
        num_count++;
    }

    num_min = num_map[numbers.substr(0, 1)];
    num_max = num_map[numbers.substr(0, 1)];

    for(num_index = 0; num_index < numbers.size(); num_index++){
        if(num_map[numbers.substr(num_index,