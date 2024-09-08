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
    for (int i = 0; i < message.length(); i++){
        char c = message[i];
        if (islower(c)){
            if (c == 'a'){
                output += 'c';
            }
            else if (c == 'e'){
                output += 'g';
            }
            else if (c == 'i'){
                output += 'k';
            }
            else if (c == 'o'){
                output += 'q';
            }
            else if (c == 'u'){
                output += 's';
            }
            else{
                output += toupper(c);
            }
        }
        else{
            if (c == 'A'){
                output += 'C';
            }
            else if (c == 'E'){
                output += 'G';
            }
            else if (c == 'I'){
                output += 'K';
            }
            else if (c == 'O'){
                output += 'Q';
            }
            else if (c == 'U'){
                output += 'S';
            }
            else{
                output += tolower(c);
            }
        }
    }
    return output;
}

C:
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
    for (int i = 0; i < message.length(); i++){
        char c = message[i];
        if (islower(c)){
            if (c == 'a'){
                output += 'c';
            }
            else if (c == 'e