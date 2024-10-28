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

    // Sort numbers from smallest to largest
    map<string, int> nums;
    for(string::iterator it = numbers.begin(); it != numbers.end(); it++){
        int num = atoi(it);
        if(num > 0){
            nums[it] = num;
        }
    }

    string sorted_numbers = "";
    for(map<string, int>::iterator it = nums.begin(); it != nums.end(); it++){
        sorted_numbers += it->first;
    }
    return sorted_numbers;
}
