/*
Write a function that takes a message, and encodes in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the english alphabet. 
Assume only letters. 

Examples:
>>> encode('test")
"TGST"
>>> encode("This is a message")
'tHKS KS C MGSSCGG"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string encode(string message){

    string output;
    for(int i = 0; i < message.size(); i++){
        if(isalpha(message[i])){
            message[i] = (islower(message[i]) ? toupper(message[i]) : tolower(message[i]));
        }
        if(isalpha(message[i]) && message[i] == 'e'){
            message[i] = 'g';
        }
    }
    return message;
}

