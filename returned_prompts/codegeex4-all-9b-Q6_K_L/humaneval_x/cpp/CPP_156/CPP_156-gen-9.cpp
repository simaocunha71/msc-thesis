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
#include<math.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int number){
    string roman="";
    vector<int> int_to_roman={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    vector<string> roman_to_int={"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    for(int i=0;i<int_to_roman.size();i++){
        while(number>=int_to_roman[i]){
            roman=roman+roman_to_int[i];
            number-=int_to_roman[i];
        }
    }
    return roman;
}