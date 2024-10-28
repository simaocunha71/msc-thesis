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
    vector<string> roman_num(1000, "");
    roman_num[1] = "i";
    roman_num[4] = "iv";
    roman_num[5] = "v";
    roman_num[9] = "ix";
    roman_num[10] = "x";
    roman_num[40] = "xl";
    roman_num[50] = "l";
    roman_num[90] = "xci";
    roman_num[100] = "c";
    roman_num[400] = "cd";
    roman_num[500] = "d";
    roman_num[900] = "cm";
    roman_num[1000] = "m";
    string roman_num_str;
    for (int i = 0; i < 1000; i++){
        int count = 0;
        while (number >= i){
            count ++;
            number -= i;
        }
        if (count > 0)
            roman_num_str += roman_num[i] + string(count, '0');
    }
    return roman_num_str;
}
int main(){
    for (int i = 1; i < 1000; i++){
        printf("%d: %s\n", i, int_to_mini_roman(i).c_str());
    }
    return 0;
}
