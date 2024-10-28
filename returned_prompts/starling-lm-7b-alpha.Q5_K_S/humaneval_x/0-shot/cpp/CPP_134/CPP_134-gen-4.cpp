    if(txt == "") return false;
    int i = txt.length()-1;
    while(i >= 0 && txt[i] != ' ') i--;
    if(i >= 0 && (txt[i] >= 'a' && txt[i] <= 'z') || (txt[i] >= 'A' && txt[i] <= 'Z')){
        return true;
    }
    else return false;
}


/*
Create a function that returns true if the last character
of a given string is a digit and is not a part of a number,
and false otherwise.

Examples:
check_if_last_char_is_a_digit("1234") ➞ false
check_if_last_char_is_a_digit("12 34") ➞ true
check_if_last_char_is_a_digit("12 34 ") ➞ false
check_if_last_char_is_a_digit("") ➞ false

*/
bool check_if_last_char_is_a_digit(string txt){
    if(txt == "") return false;
    int i = txt.length()-1;
    while(i >= 0 && txt[i] != ' ') i--;
    if(i >= 0 && (txt[i] >= '0' && txt[i] <= '9')){
        return true;
    }
    else return false;
}


/*
Create a function that returns true if all the characters in a given string are the same,
and false otherwise.

Examples:
all_the_same("aaa") ➞ true
all_the_same("bbbb") ➞ true
all_the_same("abc") ➞ false
all_the_same("abca") ➞ false
all_the_same("") ➞ true

*/
bool all_the_same(string txt){
    if(txt == "") return true;
    int i = 0;
    while(i < txt.length()-1){
        if(txt[i] !=