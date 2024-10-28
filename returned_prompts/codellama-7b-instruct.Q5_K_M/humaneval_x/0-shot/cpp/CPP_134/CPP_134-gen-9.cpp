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

    int flag=0;
    for(int i=0;i<txt.length();i++){
        if(txt[i]==' '){
            flag=1;
        }
    }
    if(flag==1){
        return false;
    }else{
        if(isalpha(txt[txt.length()-1])){
            return true;
        }else{
            return false;
        }
    }
}
