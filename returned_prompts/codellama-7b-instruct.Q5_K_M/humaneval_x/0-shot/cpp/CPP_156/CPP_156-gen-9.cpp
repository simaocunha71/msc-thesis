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
string int_to_mini_romank(int number){
    vector<string> roman_numbers = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    vector<int> roman_values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman_numeral = "";
    int i = 0;
    while(number > 0){
        while(number >= roman_values[i]){
            number -= roman_values[i];
            roman_numeral += roman_numbers[i];
        }
        ++i;
    }
    return roman_numeral;
}
