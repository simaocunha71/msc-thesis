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

vector<string> roman_numerals = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
vector<int> roman_numeral_values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
string roman_numeral = "";
int quotient = number;
while(quotient > 0){
if(quotient >= roman_numeral_values[0]){
roman_numeral = roman_numerals[0];
quotient -= roman_numeral_values[0];
}
else{
for(int i = 1; i < roman_numerals.size(); i++){
if(quotient >= roman_numeral_values[i]){
roman_numeral = roman_numerals[i];
quotient -= roman_numeral_values[i];
break;
}
}
}
}
return roman_numeral;
}
int main(){
int number = 19;
string mini_roman = int_to_mini_roman(number);
printf("%s\n", mini_roman.c_str());
return 0;
}
