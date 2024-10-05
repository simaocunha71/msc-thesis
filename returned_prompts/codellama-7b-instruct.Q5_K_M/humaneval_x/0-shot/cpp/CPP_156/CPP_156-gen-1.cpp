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
    string roman_number;
    switch(number){
        case 1: roman_number = "i"; break;
        case 5: roman_number = "v"; break;
        case 10: roman_number = "x"; break;
        case 50: roman_number = "l"; break;
        case 100: roman_number = "c"; break;
        case 500: roman_number = "d"; break;
        case 1000: roman_number = "m"; break;
        default: roman_number = ""; break;
    }
    return roman_number;
}
int main(){
    int number;
    cin >> number;
    string roman_number = int_to_mini_roman(number);
    cout << roman_number << endl;
    return 0;
}
