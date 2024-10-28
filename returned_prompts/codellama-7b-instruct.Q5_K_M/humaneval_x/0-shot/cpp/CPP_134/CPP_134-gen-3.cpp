/*
Create a function that returns true if the last character
of a given string is an alphabetical character and is not
a part of a word, and false otherwise.
Note: "word" is a group of characters separated by space.

Examples:
check_if_last_char_is_a_letter("apple pie") ➞ false
check_if_last_char_is_a_letter("apple pi e") ➞ true
check_if_last_char_is_a_letter("apple pi e ") ➞ false
check_if_last_char_is_a_letter("") ➞ false 
*/
#include<stdio.h>
#include<string>
using namespace std;
bool check_if_last_char_is_a_letter(string txt){

bool result = false;

for(int i = 0; i < txt.length() - 1; i++){
    if(txt[i] == ' '){
        result = (txt[txt.length() - 1] >= 'a' && txt[txt.length() - 1] <= 'z' || txt[txt.length() - 1] >= 'A' && txt[txt.length() - 1] <= 'Z');
    }
}

return result;
}
